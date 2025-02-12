Exercise

# 29\. Fortune Cookie

## [#](https://www.codedex.io/python/29-fortune-cookie#define-a-function) Define a Function

So how do we create a function from scratch?

User-defined functions are functions we define ourselves to do a specific task, and it's a two-step process: 1️) define and 2️) call.

To **define** a function, we need a function definition. A **function definition** begins with the `def` keyword, followed by the function name, a set of parentheses, and a colon in that order.

Here’s what a function definition looks like:

    def name():
      # The code inside
    

-   The `def` keyword.
-   The function name, followed by a pair of parentheses `()`.
-   The colon `:`.

The code inside the function is called the body of the function. And just like `if` statements and `while` loops, the code inside a function must be indented.

**Note:** The common naming convention for functions is [snake\_case](https://en.wikipedia.org/wiki/Snake_case).

Suppose we want to create a function named `say_hello()`:

    def say_hello():
      print('Howdy! 🤠')
      print('How are you?')
    

We just defined a function that prints out two greetings!

Defining a function creates the function, and it's the first step, but it doesn't mean that Python will automatically run the code inside its body. How do we convey to Python that we want the function body executed?

We need to call the function!

## [#](https://www.codedex.io/python/29-fortune-cookie#call-a-function) Call a Function

To **call** a function, we use the function name followed by parentheses somewhere in the code:

    def say_hello():
      print('Howdy! 🤠')
      print('How are you?')
    
    say_hello()
    

This executes the `say_hello()` function once!

So the output would be:

    Howdy! 🤠
    How are you?
    

We can also call a function numerous times. For example:

    def say_hello():
      print('Howdy! 🤠')
      print('How are you?')
    
    say_hello()
    say_hello()
    say_hello()
    

This executes the `say_hello()` function three times!

So the output would be:

    Howdy! 🤠
    How are you?
    Howdy! 🤠
    How are you?
    Howdy! 🤠
    How are you?
    

Now it’s your turn to define and call a function in a program!

## [#](https://www.codedex.io/python/29-fortune-cookie#instructions) Instructions

[Fortune Cookie](https://en.wikipedia.org/wiki/Fortune_cookie) is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada. 🥠

Create a **fortune\_cookie.py** program that gives the user random fortunes.

Define a function named `fortune()`. Inside the function, print out a random fortune from the list of options below:

-   `Don't pursue happiness – create it.`
-   `All things are difficult before they are easy.`
-   `The early bird gets the worm, but the second mouse gets the cheese.`
-   `Someone in your life needs a letter from you.`
-   `Don't just think. Act!`
-   `Your heart will skip a beat.`
-   `The fortune you search for is in another cookie.`
-   `Help! I'm being held prisoner in a Chinese bakery!`

Make sure to use the `random` module's `random.randint()` and an `if`/`elif`/`else`.

Then, call the `fortune()` function three times and see what you get!

**Bonus:** If you're daring, rewrite the function without an `if`/`elif`/`else`.



