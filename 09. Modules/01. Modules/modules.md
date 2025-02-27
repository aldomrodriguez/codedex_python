Exercise

# 39\. Slot Machine

## [#](https://www.codedex.io/python/39-slot-machine#modules) Modules

Welcome to the final chapter of The Legend of Python! 🐍

Here, we are going to take a deep dive into something called modules.

A **module** is any file with a **.py** extension. But more ideally, a module contains statements, functions, and class definitions that revolve around a similar purpose.

By default, Python comes with [over 200 modules](https://docs.python.org/3/py-modindex.html) that we can use.

Here are some examples:

-   [`random`](https://docs.python.org/3/library/random.html) module to generate a random number.
-   [`math`](https://docs.python.org/3/library/math.html) module to calculate the square root.
-   [`datetime`](https://docs.python.org/3/library/datetime.html) module to work with dates and times.

Modules are magical because they offer us tools and method to solve a problem that we'd otherwise have to write ourselves.

In this chapter, we will use built-in modules first before creating our own.

## [#](https://www.codedex.io/python/39-slot-machine#random-choices) Random Choices

Let's revisit a module we've already worked with before: the `random` module!

Remember when we used the `.randint()` method to generate a random number in the [Magic 8 Ball](https://www.codedex.io/python/14-magic-8-ball#random)? Well, there are 22 methods total in the `random` module.

Here's another method, `.choices()`, in action:

    import random
    
    dice = [1, 2, 3, 4, 5, 6]
    
    print(random.choices(dice))
    

-   The `import` keyword is used to access the `random` module.
-   The `.choices()` method will randomly select a single item by default.

We can also set how many items are randomly chosen with the `k` parameter:

    import random
    
    dice = [1, 2, 3, 4, 5, 6]
    
    print(random.choices(dice, k=3))
    

This will return a new list of three items randomly selected from `dice`. Every time you run it, the output should be different.

**Note:** The `k` parameter only sets the _length_ of the returned list from `.choices()`. This means that a list item may be included in the returned list more than once.

## [#](https://www.codedex.io/python/39-slot-machine#multiple-modules) Multiple Modules

There are two ways to import two or more modules at the top of our program:

1.  With multiple `import` statements:

    import random
    import math
    
    # Rest of the code...
    

2.  With one `import` statement and modules separated by commas:

    import random, math
    
    # Rest of the code...
    

These two code blocks do the exact same thing.

## [#](https://www.codedex.io/python/39-slot-machine#instructions) Instructions

A gambling machine was invented in Brooklyn around 1891. Players would insert a nickel and pull a lever. If it's a good poker hand, you win a free beer. Soon, many bars in the city had it. This was a precursor to the modern [slot machine](https://en.wikipedia.org/wiki/Slot_machine).

Create a **slot\_machine.py** program using `random`.

The items are symbols of common fruits and sevens (7️⃣). In each round, the slot machine displays three random items. If there are three sevens, you win!

![Final Program Output](https://www.codedex.io/images/python/39_slot_machine.gif)

Create a `symbols` list and include the following items: `'🍒'`,`' 🍇'`, `'🍉'`, `'7️⃣'`.

Next, create a `results` variable that uses the `.choices()` method from the `random` module and get three random symbols. Make sure to import the required module at the top of the file!

Then, print each value from `results`, separated by `|` pipe characters:

    🍉 | 🍒 | 🍇
    

Lastly, use an `if`/`else` statement:

-   If all of the list items in `results` are equal to `'7️⃣'`, print "Jackpot! 💰".
-   Else, print "Thanks for playing!".

**Bonus:**

-   Rewrite this program with a `play()` function.
-   Add a `while` loop for the player to keep playing, round after round.
-   Ask the player for a `'Y'` or `'N'` input to keep playing with `input()`.

