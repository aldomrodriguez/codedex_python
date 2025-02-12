# 32\. Stonks

## [#](https://www.codedex.io/python/32-stonks#scope) Scope

Suppose we created a variable inside the body of a function. Can we use it outside of the function? Well, let's see.

Define a function named `add()` and print the variable `answer` outside of it:

    def add(x, y):
      answer = x + y
      return answer
    
    print(answer)
    

When we run this code, we will get an error:

    NameError: name 'answer' is not defined
    

This is due to something called scope.

**Scope** determines where in the program a variable is visible and can be used.

Here are two types of scope:

-   The scope of the `answer` variable is only inside the `add()` function. It is a **local variable** that belongs to the **local scope** of the `add()` function.
-   Now, a variable created outside of a function is called a **global variable** and belongs to the **global scope**, meaning that they can be used by every function.

Let's try setting the `answer` variable as a global variable (outside the function):

    answer = 0
    
    def add(x, y):
      answer = x + y
      return answer
    
    add(3, 4)
    
    print(answer)
    

The output won't be an error anymore!

    0
    

Notice that `answer` is not 7. It's still 0 because if we create a variable with the same name inside a function, it will be a local variable and can only be used inside the function. The global variable with the same name will remain global and with the original value.

## [#](https://www.codedex.io/python/32-stonks#instructions) Instructions

In fintech, we often perform a [time series analysis](https://en.wikipedia.org/wiki/Time_series) on stocks. This means that we need to analyze a stock, given its price over a certain time. 📈

In this exercise, we will perform a simplified version of a time series analysis. The stock that we will be analyzing is the [$AMC](https://www.google.com/search?q=amc+stock+prices) stock in January 2023.

Here are the stock prices (in dollars) for each of these weekdays:

    stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]
    

Create a **stock\_analysis.py** program that implements three functions:

-   `price_at(x)` that finds the price on a given day `x`.
-   `max_price(a, b)` that finds the maximum price from day `a` to day `b`.
-   `min_price(a, b)` that finds the minimum price from day `a` to day `b`.

The parameters of the days will be in the range of 1 to 20 (since that is the period for the stock we are analyzing).

Make sure to call each function to test if your functions work correctly!



