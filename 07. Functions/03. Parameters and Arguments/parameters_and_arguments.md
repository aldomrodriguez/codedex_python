# 30\. Mars Orbiter

## [#](https://www.codedex.io/python/30-mars-orbiter#parameters-and-arguments) Parameters and Arguments

So far, the functions we've created don't take in any input(s), which means they do the same thing each time they get called. A function can be far more useful than that!

Sometimes, we want our functions to perform a specific task, but the task varies depending on different input(s). And that's where parameters come in.

**Parameters** are variables that a function takes in as input. They go inside the parentheses in the function definition and are used inside the function.

For example, suppose we define and call a `happy_birthday()` function like so:

    def happy_birthday():
      print('Happy birthday to you')
      print('Happy birthday to you')
      print('Happy birthday dear friend')
      print('Happy birthday to you')
    
    happy_birthday()
    

This prints out the same thing every time.

Let's say we want to make the song more personalized. For example, say the person's name instead of just “dear friend”, then we can do this:

    def happy_birthday(name):
      print('Happy birthday to you')
      print('Happy birthday to you')
      print('Happy birthday dear ' + name )
      print('Happy birthday to you')
    

Here, we gave the `happy_birthday()` function a `name` parameter for the function to take in. So we can use the `name` variable within the function body.

And later in the program, when we call the `happy_birthday()` function, we can add an argument in the call.

An **argument** is the value sent to the function when the function is called.

    happy_birthday('Lillian')
    

The output would be:

    Happy birthday to you
    Happy birthday to you
    Happy birthday dear Lillian
    Happy birthday to you
    

So what's the difference between a parameter and an argument? Why are there two words for the same thing?

-   The parameter is the variable listed inside the parenthesis in the function definition (when we define the function).
-   The argument is the value sent to the function (when we call the function).

In the example above, the variable `name` is the parameter, and the value `'Lillian'` is the argument.

By the way, we’ve already been using arguments all along, when calling the `print()` function for instance. In a `print('Yo!')`, the `'Yo!'` is the argument.

## [#](https://www.codedex.io/python/30-mars-orbiter#instructions) Instructions

In September 1999, after ten months of travel to Mars, the [Mars Climate Orbiter](https://en.wikipedia.org/wiki/Mars_Climate_Orbiter) suddenly burned to pieces because it had entered the atmosphere too fast.

Oh no! The NASA engineers forgot to convert imperial data to metric data in one of the functions! This noob mistake cost American taxpayers $125 million total.

Suppose you're a [NASA intern](https://www.codedex.io/blog/a-day-in-the-life-swe-intern-nasa-brandon-lam), and your team is calculating the distance a rocket needs to travel. The value calculated is in kilometers, while the next step requires miles. Your manager quickly writes this on the board:

  

miles\=kilometer1.609miles = {kilometer\\over 1.609}miles\=1.609kilometer​

  

Create a new file called **rocket.py**.

Define a function named `distance_to_miles()` that converts a distance from kilometers to miles. It should:

-   Take in one parameter named `distance` (the distance in kilometers).
-   Print the distance in miles.

After, call the function and use `10000` as the argument.



