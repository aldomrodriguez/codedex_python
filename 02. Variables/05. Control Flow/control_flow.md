# 11\. Coin Flip

## [#](https://www.codedex.io/python/11-coin-flip#control-flow) Control Flow

So far, every Python program we've encountered has only had one path of execution — they all execute one line at a time, from top to bottom. Every time you run them, it gives you the same result.

Sometimes, we want our program to do different things based on different conditions.

It's like going down a highway and there's a fork ahead with a sign that reads "Albuquerque: left. Phoenix: right."

![](https://www.codedex.io/images/fork.png)

In the "Control Flow" chapter, we will explore how programs "make decisions" by evaluating different conditions. And start introducing logic into our code!

## [#](https://www.codedex.io/python/11-coin-flip#instructions) Instructions

Before we dive deep into something called an `if` statement, let's do a fun demo using a coin flip simulation!

Create a **coin\_flip.py** program and type in the following:

    import random
    
    num = random.randint(0, 1)   # Generates a random number that's either 0 or 1
    
    if num > 0.5:
      print('Heads')
    else:
      print('Tails')
    

**Note:** We will learn more about `random` and `.randint()` later in the chapter.

All you need to know is that this program simulates a coin toss:

-   ≈ 50% of the time, it's "Heads".
-   ≈ 50% of the time, it's "Tails".

![](https://www.codedex.io/images/pixel_coin_flip.gif)

Run the program 5 times to get a taste of the `if`/`else` statement!

How many times did it go Heads?



