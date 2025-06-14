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
