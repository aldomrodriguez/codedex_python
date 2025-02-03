# 14\. Magic 8 Ball

## [#](https://www.codedex.io/python/14-magic-8-ball#random) Random

In Python, modules are **.py** files containing Python code that can be imported inside another Python program. The Python standard library contains well over 200 modules that we can use.

We can use the `.randint()` function from a module called `random` to generate a random number from a range.

But first, let's import this module so we can use its functions.

    import random
    

Next, we'll create a variable to store the randomly generated value. Declare a variable called `num`, and assign it to the function call:

    num = random.randint(1, 9)
    

This will generate a random number between 1 and 9 (inclusive of both).

Together, the code will look like:

    import random
    
    num = random.randint(1, 9)
    
    print(num)
    

Try running this code! ☝️

The output should be different each time it runs: 2, 8, 5, 9, 2, 1, 3...

## [#](https://www.codedex.io/python/14-magic-8-ball#instructions) Instructions

The [Magic 8 Ball](https://en.wikipedia.org/wiki/Magic_8_ball) is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

-   `Yes - definitely.`
-   `It is decidedly so.`
-   `Without a doubt.`
-   `Reply hazy, try again.`
-   `Ask again later.`
-   `Better not tell you now.`
-   `My sources say no.`
-   `Outlook not so good.`
-   `Very doubtful.`

Create a **magic8.py** program that can respond to any Yes or No questions with a different answer each time it executes.

The output should have the following format:

    Question:      [Question]
    Magic 8 Ball:  [Answer]
    

For example:

    Question:      Is Codédex better than Udemy yet?
    Magic 8 Ball:  Better not tell you now.
    

### Help



