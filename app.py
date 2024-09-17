import os
import random
import re
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from textblob import TextBlob
import getpass
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

# Logging setup
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Retrieve the Hugging Face API token from environment variables
api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")

# Check if the API key is loaded correctly
if not api_key:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found. Please check your .env file.")

llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.3",
    task="text-generation",
    max_length=10,
    temperature=0.4,
    huggingfacehub_api_token=api_key,
)

min_price = 190
max_price = 200
current_price = max_price
# You are a skilled salesperson negotiating the price of a product. 
#     The customer said: "{user_message}"
#     Your current asking price is ${current_price}
#     You want to make a counteroffer of ${counter_offer}
#     The customer's message sentiment is {sentiment} (positive, neutral, or negative). 
prompt_template = PromptTemplate(
    input_variables=["user_message", "current_price", "counter_offer", "sentiment"],
    template="""
    You are a skilled salesperson negotiating the price of a product. 
    The customer said: "{user_message}"
    Your current asking price is ${current_price}
    You want to make a counteroffer of ${counter_offer}
    The customer's message sentiment is {sentiment} (positive, neutral, or negative).
    Respond with a single, concise sentence that:
    - Acknowledges the customer's message and sentiment.
    - Politely suggests your counteroffer of ${counter_offer}.
    - Gives a reason why this price is fair.
    - If the sentiment is positive, express appreciation for their politeness.
    """
)

chain = LLMChain(llm=llm, prompt=prompt_template)

class Offer(BaseModel):
    message: str="The current_price is 200"

def extract_price(text):
    match = re.search(r'\$?(\d+(?:\.\d{2})?)', text)
    if match:
        return float(match.group(1))
    return None

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"

@app.post('/negotiate')
async def negotiate(offer: Offer):
    global current_price
    user_message = offer.message
    extracted_price = extract_price(user_message)
    sentiment = analyze_sentiment(user_message)

    if extracted_price is not None:
        user_offer = extracted_price
        if user_offer >= current_price:
            response = f"Great! We have a deal. The price is agreed at ${user_offer}"
            current_price = max_price
            return {"response": response, "current_price": current_price, "detected_sentiment": sentiment}
        elif user_offer < min_price:
            response = f"I'm sorry, but that offer is too low. Our minimum price is ${min_price}"
            return {"response": response, "current_price": current_price, "detected_sentiment": sentiment}

    base_counter_offer = round(random.uniform(max(min_price, extracted_price or min_price), current_price), 2)

    if sentiment == "positive":
        counter_offer = max(min_price, base_counter_offer * 0.95)
    else:
        counter_offer = base_counter_offer
    
    counter_offer = round(counter_offer, 2)

    try:
        ai_response = chain.run(user_message=user_message, current_price=current_price, counter_offer=counter_offer, sentiment=sentiment)
        logging.debug(f"Raw AI response: {ai_response}")
        response = ai_response.replace("Your response:", "").strip()
    except Exception as e:
        logging.error(f"Error generating AI response: {e}")
        response = f"Thank you for your message. Our current price is ${current_price}. How about we meet in the middle at ${counter_offer}?"
    
    current_price = counter_offer
    return {"response": response, "current_price": current_price, "detected_sentiment": sentiment}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
