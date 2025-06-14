# **Chapter 4: Random Variables**

This document provides a comprehensive overview of random variables, their properties, and various discrete probability distributions. Understanding these concepts is fundamental to probability theory and its applications.

## **4.1 Random Variables**

A **random variable** is a function that assigns a numerical value to each outcome in the sample space of a random experiment. Random variables are typically denoted by uppercase letters (e.g., X,Y,Z), and their observed values by lowercase letters (e.g., x,y,z).

**Key Idea:** Instead of dealing with the potentially non-numerical outcomes of an experiment (like "Heads" or "Tails," or the specific card drawn), a random variable allows us to analyze experiments using numerical values, which makes mathematical analysis much easier.

Example 4.1.1:  
Consider the experiment of tossing a coin three times. The sample space S is:  
S=HHH,HHT,HTH,THH,HTT,THT,TTH,TTT  
Let X be the random variable representing the number of heads in three tosses.

* X(HHH)=3  
* X(HHT)=2  
* X(HTH)=2  
* X(THH)=2  
* X(HTT)=1  
* X(THT)=1  
* X(TTH)=1  
* X(TTT)=0

The possible values for X are 0,1,2,3.

**Types of Random Variables:**

1. **Discrete Random Variables:** A random variable is **discrete** if its set of possible values is finite or countably infinite. This means the values can be listed, even if the list is infinite (like the set of positive integers).  
   * **Examples:**  
     * Number of heads in N coin tosses.  
     * Number of cars passing a point on a highway in an hour.  
     * Number of defective items in a sample.  
2. **Continuous Random Variables:** A random variable is **continuous** if its set of possible values is an entire interval of real numbers. These variables can take on any value within a given range.  
   * **Examples:**  
     * Height of a person.  
     * Time it takes for a bus to arrive.  
     * Temperature of a room.

This chapter primarily focuses on **discrete random variables**.

## **4.2 Discrete Random Variables**

For a discrete random variable X, we are interested in the probability that X takes on each of its possible values. This is described by the **probability mass function (PMF)**, denoted as p(x) or P(X=x).

The PMF p(x) for a discrete random variable X satisfies the following properties:

1. 0≤p(x)≤1 for all possible values x.  
2. ∑x​p(x)=1, where the sum is over all possible values of x.

Example 4.2.1 (Continuing from Example 4.1.1):  
For X \= number of heads in three coin tosses:

* P(X=0)=P(TTT)=1/8  
* P(X=1)=P(HTT,THT,TTH)=3/8  
* P(X=2)=P(HHT,HTH,THH)=3/8  
* P(X=3)=P(HHH)=1/8

So, the PMF is:  
p(0)=1/8  
p(1)=3/8  
p(2)=3/8  
p(3)=1/8  
We can verify the properties:

1.  All  $p(x)$ values are between $0$ and $1$.
2. $ ∑p(x)=1/8+3/8+3/8+1/8=8/8=1.$

## **4.3 Expected Value**

The **expected value** or **mean** of a discrete random variable X, denoted by E\[X\] or μX​, is a weighted average of the possible values that X can take, where the weights are the probabilities of those values. It represents the long-run average value of the random variable if the experiment were to be repeated many times.

For a discrete random variable X with PMF p(x), the expected value is defined as:

E\[X\]=x∑​x⋅p(x)  
Example 4.3.1 (Continuing from Example 4.1.1):  
For X \= number of heads in three coin tosses:  
E\[X\]=(0⋅p(0))+(1⋅p(1))+(2⋅p(2))+(3⋅p(3))  
E\[X\]=(0⋅1/8)+(1⋅3/8)+(2⋅3/8)+(3⋅1/8)  
E\[X\]=0+3/8+6/8+3/8=12/8=3/2=1.5  
This means that if you toss three coins many times, on average, you would expect to get 1.5 heads per three tosses.

**Properties of Expected Value:**

* E\[c\]=c for any constant c.  
* E\[cX\]=cE\[X\] for any constant c.  
* E\[X+Y\]=E\[X\]+E\[Y\] (Linearity of Expectation \- true even if X and Y are not independent, discussed in 4.9).

## **4.4 Expectation of a Function of a Random Variable**

If X is a discrete random variable with PMF p(x), and g(X) is some function of X, then g(X) is also a random variable. The expected value of g(X) is given by:

E\[g(X)\]=x∑​g(x)⋅p(x)

where the sum is over all possible values of X.  
Example 4.4.1:  
Let X be the random variable representing the outcome of rolling a fair six-sided die.  
The PMF for X is p(x)=1/6 for x∈1,2,3,4,5,6.  
Let g(X)=X2. We want to find E\[X2\].  
E\[X2\]=∑x=16​x2⋅p(x)  
E\[X2\]=(12⋅1/6)+(22⋅1/6)+(32⋅1/6)+(42⋅1/6)+(52⋅1/6)+(62⋅1/6)  
E\[X2\]=(1/6)⋅(1+4+9+16+25+36)  
E\[X2\]=(1/6)⋅(91)=91/6≈15.17

## **4.5 Variance**

The **variance** of a random variable X, denoted by Var(X) or σX2​, is a measure of how spread out the values of the random variable are around its expected value (mean). A high variance indicates that the values are widely dispersed, while a low variance indicates that they are clustered closely around the mean.

The variance is defined as the expected value of the squared difference between the random variable and its mean:

Var(X)=E\[(X−E\[X\])2\]  
Using the linearity of expectation, we can derive an alternative (and often more convenient) formula:

Var(X)=E\[X2\]−(E\[X\])2  
The standard deviation of X, denoted by SD(X) or σX​, is the square root of the variance:

SD(X)=Var(X)​

The standard deviation is in the same units as the random variable itself, making it easier to interpret than the variance.  
Example 4.5.1 (Continuing from Example 4.3.1 and 4.4.1 values):  
For X \= number of heads in three coin tosses:  
We found E\[X\]=1.5.  
Now let's find E\[X2\]:  
E\[X2\]=(02⋅1/8)+(12⋅3/8)+(22⋅3/8)+(32⋅1/8)  
E\[X2\]=(0⋅1/8)+(1⋅3/8)+(4⋅3/8)+(9⋅1/8)  
E\[X2\]=0+3/8+12/8+9/8=24/8=3  
Now, calculate the variance:  
Var(X)=E\[X2\]−(E\[X\])2  
Var(X)=3−(1.5)2=3−2.25=0.75  
The standard deviation is:  
SD(X)=0.75​≈0.866  
**Properties of Variance:**

* Var(c)=0 for any constant c (a constant has no variability).  
* Var(cX)=c2Var(X) for any constant c.  
* Var(X+c)=Var(X) (adding a constant shifts the distribution but doesn't change its spread).  
* If X and Y are independent random variables, then Var(X+Y)=Var(X)+Var(Y). (Note: This is not true in general if X and Y are dependent.)

## **4.6 The Bernoulli and Binomial Random Variables**

### **The Bernoulli Random Variable**

A Bernoulli trial is a single experiment that has only two possible outcomes: "success" or "failure."  
Let p be the probability of success, and 1−p be the probability of failure.  
A random variable X is a Bernoulli random variable if it takes the value 1 for success and 0 for failure.  
Its PMF is:  
P(X=1)=p  
P(X=0)=1−p

* **Mean of Bernoulli:** E\[X\]=1⋅p+0⋅(1−p)=p  
* **Variance of Bernoulli:** Var(X)=E\[X2\]−(E\[X\])2=(12⋅p+02⋅(1−p))−p2=p−p2=p(1−p)

### **The Binomial Random Variable**

A Binomial random variable represents the number of successes in a fixed number of independent Bernoulli trials.  
Let n be the number of trials and p be the probability of success in each trial.  
A random variable X follows a Binomial distribution if it satisfies these conditions:

1. There is a fixed number of trials, n.  
2. Each trial is independent.  
3. Each trial has only two outcomes: success or failure.  
4. The probability of success, p, is the same for each trial.

The notation for a Binomial random variable is X∼B(n,p).

The PMF of a Binomial random variable X (the probability of getting exactly k successes in n trials) is:

P(X=k)=(kn​)pk(1−p)n−kfor k=0,1,…,n

where (kn​)=k\!(n−k)\!n\!​ is the binomial coefficient, representing the number of ways to choose k successes from n trials.

* **Mean of Binomial:** E\[X\]=np  
* **Variance of Binomial:** Var(X)=np(1−p)

Example 4.6.1:  
Suppose a basketball player makes a free throw with a probability of p=0.7. If she takes n=5 free throws, what is the probability that she makes exactly 3 of them?  
Let X be the number of successful free throws. X∼B(5,0.7).  
P(X=3)=(35​)(0.7)3(1−0.7)5−3  
P(X=3)=3\!2\!5\!​(0.7)3(0.3)2  
P(X=3)=10⋅(0.343)⋅(0.09)  
P(X=3)=10⋅0.03087=0.3087  
Expected number of successes: E\[X\]=np=5⋅0.7=3.5  
Variance of successes: Var(X)=np(1−p)=5⋅0.7⋅0.3=1.05

### **4.6.1 Properties of Binomial Random Variables**

1. Sum of Binomials: If X1​∼B(n1​,p) and X2​∼B(n2​,p) are independent binomial random variables with the same probability of success p, then their sum X1​+X2​ is also a binomial random variable:  
   X1​+X2​∼B(n1​+n2​,p)  
   This property makes intuitive sense: if you perform n1​ trials and then n2​ more trials, and each trial has the same success probability, the total number of successes is simply the sum of successes from both sets of trials.  
2. **Approximation by Normal Distribution:** For large n, the Binomial distribution can be approximated by the Normal distribution (Central Limit Theorem). This is particularly useful for calculations when n is very large.

### **4.6.2 Computing the Binomial Distribution Function**

The cumulative distribution function (CDF) for a discrete random variable X, denoted by F(x), gives the probability that X takes on a value less than or equal to x. For a Binomial random variable, this is:

F(k)=P(X≤k)=i=0∑k​(in​)pi(1−p)n−i

Calculating P(X≤k) often involves summing multiple PMF values. For large n, tables or statistical software are used.

## **4.7 The Poisson Random Variable**

The **Poisson random variable** is often used to model the number of events occurring in a fixed interval of time or space, when these events occur with a known constant mean rate and independently of the time since the last event. It is a good model for rare events.

Examples of events often modeled by a Poisson distribution:

* Number of calls arriving at a call center per hour.  
* Number of defects per square meter of fabric.  
* Number of car accidents at an intersection per month.  
* Number of radioactive decays per second.

A random variable X follows a Poisson distribution if its PMF is:

P(X=k)=k\!e−λλk​for k=0,1,2,…

where λ (lambda) is the average number of events in the given interval (also the mean and variance of the distribution).  
The notation for a Poisson random variable is X∼Poisson(λ).

* **Mean of Poisson:** E\[X\]=λ  
* **Variance of Poisson:** Var(X)=λ

**Relationship to Binomial:** The Poisson distribution can be derived as a limiting case of the Binomial distribution when the number of trials n is very large, the probability of success p is very small, and the product np (which is the expected number of successes) remains constant and equal to λ. That is, if n→∞, p→0, and np→λ, then B(n,p)→Poisson(λ).

Example 4.7.1:  
A support center receives an average of 3 calls per hour. What is the probability that they receive exactly 5 calls in the next hour?  
Here, λ=3. We want P(X=5).  
P(X=5)=5\!e−335​=1200.049787⋅243​≈12012.098​≈0.1008

### **4.7.1 Computing the Poisson Distribution Function**

Similar to the Binomial, the CDF for a Poisson random variable gives the probability of observing up to k events:

F(k)=P(X≤k)=i=0∑k​i\!e−λλi​

Again, for practical calculation of P(X≤k), especially for larger k, statistical software or tables are used.

## **4.8 Other Discrete Probability Distributions**

### **4.8.1 The Geometric Random Variable**

A Geometric random variable models the number of independent Bernoulli trials required to get the first success.  
Let p be the probability of success on any given trial.  
The possible values for a Geometric random variable X are k=1,2,3,… (the first success occurs on the 1st, 2nd, 3rd, etc., trial).  
The PMF of a Geometric random variable X is:

P(X=k)=(1−p)k−1pfor k=1,2,3,…

This means that for the first success to occur on the k-th trial, there must be k−1 failures followed by 1 success.

* **Mean of Geometric:** E\[X\]=1/p  
* **Variance of Geometric:** Var(X)=(1−p)/p2

Example 4.8.1:  
If the probability of hitting a target is p=0.2, what is the probability that the first hit occurs on the 4th shot?  
P(X=4)=(1−0.2)4−1⋅0.2=(0.8)3⋅0.2=0.512⋅0.2=0.1024  
Expected number of shots to get the first hit: E\[X\]=1/0.2=5 shots.

### **4.8.2 The Negative Binomial Random Variable**

A Negative Binomial random variable generalizes the Geometric distribution. It models the number of independent Bernoulli trials required to get the r-th success (where r is a fixed positive integer).  
Let p be the probability of success on any given trial.  
The possible values for a Negative Binomial random variable X are k=r,r+1,r+2,… (at least r trials are needed for r successes).  
The PMF of a Negative Binomial random variable X (number of trials until the r-th success) is:

P(X=k)=(r−1k−1​)pr(1−p)k−rfor k=r,r+1,r+2,…

The logic behind this formula is that for the r-th success to occur on the k-th trial, there must have been exactly r−1 successes in the previous k−1 trials, and the k-th trial must be a success.

* **Mean of Negative Binomial:** E\[X\]=r/p  
* **Variance of Negative Binomial:** Var(X)=r(1−p)/p2

Note: Some definitions of the Negative Binomial random variable describe the number of *failures* before the r-th success. The given formula is for the *total number of trials*.

Example 4.8.2:  
A baseball player has a batting average of 0.300 (p=0.3). What is the probability that he gets his 2nd hit (r=2) on his 5th at-bat (k=5)?  
P(X=5)=(2−15−1​)(0.3)2(1−0.3)5−2  
P(X=5)=(14​)(0.3)2(0.7)3  
P(X=5)=4⋅0.09⋅0.343=4⋅0.03087=0.12348

### **4.8.3 The Hypergeometric Random Variable**

The **Hypergeometric random variable** is used when selecting a sample *without replacement* from a finite population where items can be classified into two categories (e.g., "success" and "failure"). This is in contrast to the Binomial distribution, which assumes selection *with replacement* or an infinite population, ensuring independence.

Consider a population of N items, containing m "success" items and N−m "failure" items. If we draw a sample of n items without replacement, let X be the number of "success" items in the sample.

The PMF of a Hypergeometric random variable X is:

P(X=k)=(nN​)(km​)(n−kN−m​)​

where:

* N: total number of items in the population.  
* m: total number of "success" items in the population.  
* n: number of items drawn in the sample.  
* k: number of "success" items in the sample (max(0,n−(N−m))≤k≤min(n,m)).  
* **Mean of Hypergeometric:** E\[X\]=nNm​  
* Variance of Hypergeometric: Var(X)=nNm​NN−m​N−1N−n​  
  The term N−1N−n​ is called the finite population correction factor. It approaches 1 as N becomes very large relative to n, at which point the Hypergeometric distribution approximates the Binomial.

Example 4.8.3:  
An urn contains 10 balls: 6 red (success) and 4 blue (failure). If 3 balls are drawn without replacement, what is the probability of drawing exactly 2 red balls?  
Here, N=10, m=6, N−m=4, n=3, k=2.  
P(X=2)=(310​)(26​)(3−24​)​=(310​)(26​)(14​)​  
(26​)=2⋅16⋅5​=15  
(14​)=4  
(310​)=3⋅2⋅110⋅9⋅8​=10⋅3⋅4=120  
P(X=2)=12015⋅4​=12060​=0.5

### **4.8.4 The Zeta (or Zipf) Distribution**

The **Zeta distribution** (also known as the Zipf distribution, especially in linguistics and information science) is a discrete probability distribution that arises in the context of power laws. It is used to model phenomena where the probability of an event is inversely proportional to some power of its rank.

If X follows a Zeta distribution with parameter s\>1, its PMF is:

P(X=k)=ζ(s)ks1​for k=1,2,3,…

where ζ(s)=∑j=1∞​js1​ is the Riemann Zeta function, which serves as the normalization constant to ensure the probabilities sum to 1\.  
**Applications:**

* **Zipf's Law:** In linguistics, it describes the frequency of words in a corpus, where the most frequent word appears approximately twice as often as the second most frequent, three times as often as the third, and so on.  
* Population sizes of cities, income distributions, and web link popularity.  
* **Mean of Zeta:** E\[X\]=ζ(s)ζ(s−1)​ for s\>2.  
* Variance of Zeta: Var(X)=ζ(s)ζ(s−2)​−(ζ(s)ζ(s−1)​)2 for s\>3.  
  Note that the mean and variance only exist for certain values of s.

## **4.9 Expected Value of Sums of Random Variables**

A very important and powerful property in probability is the **linearity of expectation**. It states that the expected value of the sum of random variables is equal to the sum of their individual expected values, regardless of whether the random variables are independent or dependent.

For any random variables X1​,X2​,…,Xn​:

E\[X1​+X2​+…+Xn​\]=E\[X1​\]+E\[X2​\]+…+E\[Xn​\]  
This property simplifies many calculations.

Example 4.9.1:  
Consider n indicator random variables Ii​, where Ii​=1 if event Ai​ occurs, and Ii​=0 otherwise.  
Then E\[Ii​\]=P(Ai​).  
If X is the total number of events that occur, then X=∑i=1n​Ii​.  
By linearity of expectation:  
E\[X\]=E\[∑i=1n​Ii​\]=∑i=1n​E\[Ii​\]=∑i=1n​P(Ai​)  
This is particularly useful for problems where calculating the PMF of X directly is difficult. For example, in the case of the Binomial distribution, we can think of X as the sum of n independent Bernoulli random variables. If Xi​ is 1 for a success on the i-th trial and 0 for a failure, then E\[Xi​\]=p.  
So, for X∼B(n,p), X=∑i=1n​Xi​, and E\[X\]=∑i=1n​E\[Xi​\]=∑i=1n​p=np. This provides an easy derivation for the mean of the Binomial distribution.

## **4.10 Properties of the Cumulative Distribution Function**

The cumulative distribution function (CDF) of a random variable X, denoted by F(x), gives the probability that the random variable X takes on a value less than or equal to x.  
For a discrete random variable X with possible values x1​\<x2​\<…\<xn​\<…, and PMF p(x), the CDF is:

F(x)=P(X≤x)=xi​≤x∑​p(xi​)  
**Properties of the CDF for any random variable (discrete or continuous):**

1. **Monotonically Non-decreasing:** If a\<b, then F(a)≤F(b). As x increases, the cumulative probability cannot decrease.  
2. **Limits:**  
   * limx→−∞​F(x)=0 (The probability of X being less than or equal to an infinitely small number is 0).  
   * limx→+∞​F(x)=1 (The probability of X being less than or equal to an infinitely large number is 1).  
3. Right-Continuity: The CDF is always right-continuous. That is, F(x)=limh→0+​F(x+h).  
   For discrete random variables, the CDF is a step function, with jumps at the possible values of X.  
   * P(X=x)=F(x)−F(x−), where F(x−) is the limit of F(y) as y approaches x from the left. This is the size of the jump at x.

**How to use CDF for probabilities:**

* P(X≤a)=F(a)  
* P(X\>a)=1−P(X≤a)=1−F(a)  
* P(a\<X≤b)=F(b)−F(a)  
* For discrete variables, P(X\<a)=F(a−) (the value of the CDF just before the jump at a).  
* For discrete variables, P(a≤X≤b)=F(b)−F(a−)

## **Summary**

This chapter introduced the fundamental concept of **random variables**, which map outcomes of random experiments to numerical values. We distinguished between **discrete** and **continuous** random variables. For discrete random variables, the **probability mass function (PMF)** describes the probability of each specific value, while the **cumulative distribution function (CDF)** gives the probability of being less than or equal to a certain value.

Key concepts explored include:

* **Expected Value (**E\[X\]**):** The mean or long-run average of a random variable.  
* **Variance (**Var(X)**):** A measure of the spread or dispersion of the random variable's values around its mean.  
* **Standard Deviation (**SD(X)**):** The square root of the variance, providing spread in the original units.  
* **Linearity of Expectation:** A powerful property stating that the expectation of a sum is the sum of expectations, regardless of independence.

We then delved into several important discrete probability distributions:

* **Bernoulli:** For a single trial with two outcomes (success/failure).  
* **Binomial:** For the number of successes in a fixed number of independent Bernoulli trials.  
* **Poisson:** For the number of rare events in a fixed interval of time or space.  
* **Geometric:** For the number of trials until the first success.  
* **Negative Binomial:** For the number of trials until the r-th success.  
* **Hypergeometric:** For the number of successes in a sample drawn without replacement from a finite population.  
* **Zeta (Zipf):** For power-law distributions, often seen in ranking phenomena.

Understanding these distributions and properties provides a robust framework for modeling and analyzing various random phenomena.
