# 31\. Calculator

## [#](https://www.codedex.io/python/31-calculator#return-value) Return Value

We learned that functions can take in inputs, but did you know that functions can also have outputs? In fact, every Python function has an output!

The `return` keyword is used to terminate a function and output a value:

    def function_name():
      # The code inside
      return value
    

When we don't add it, Python will implicitly return the default value, `None`, as the return value.

When we _do_ want to be explicit:

    def add(x, y):
      answer = x + y
      return answer
    

So a `return` keyword is added, plus the variable we want to output.

Now when we call the function, there will be an output that we can play with:

    total = add(4.99, 9.99)   # total is 14.98
    

This means that we can actually print out a function call! 💡

    print(add(3, 4))          # Same thing as print(7)
    print(add(1, 5))          # Same thing as print(6)
    print(add(5, 3))          # Same thing as print(8)
    

Here, the `add()` function is returning a value and that returned value is an argument for the `print()` function.

The output would be:

    7
    6
    8
    

**Note:** When a `return` statement is reached, Python will stop the execution of the current function, sending a value out to where the function was called.

## [#](https://www.codedex.io/python/31-calculator#print-vs-return) Print vs. Return

Now you might wonder, why are we returning values instead of printing them?

Well, `print()` functions can be anywhere in the program — inside or outside of a function, whereas `return` is the output of a function; you don't need to print out whatever you are returning.

As a rule of thumb:

-   Use `return` in a function when you want to send value(s) from one point in the code to another.
-   Use `print()` in a function when you want to display some text to the user.

## [#](https://www.codedex.io/python/31-calculator#instructions) Instructions

Let's try a classic Computer Science project: simple calculator program! 🔢

Create a **calculator.py** program and define these five functions:

-   `add(a, b)` that adds two numbers `a` and `b`.
-   `subtract(a, b)` that subtracts two numbers `a` and `b`
-   `multiply(a, b)` that multiplies two numbers `a` and `b`.
-   `divide(a, b)` that divides two numbers `a` and `b`.
-   `exp(a, b)` that takes `a` to the exponent (or power) of `b`.

Make sure to return the result in each function definition.

Test your calculator by calling each function once to make sure that it works!



