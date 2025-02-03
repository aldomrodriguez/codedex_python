## [#](https://www.codedex.io/python/08-bmi#exponents) Exponents

Python can also perform exponentiation such as 2³ or 10².

In written math, we might see an exponent as a superscript number (like above), but typing superscripts isn't always easy on modern keyboards. Since exponentiation is super similar to multiplication, Python uses the notation `**`.

So `2 ** 3` is 2³ and `10 ** 2` is 10².

Here are more examples:

    score = 2 ** 2      # score is 4
    score = 2 ** 3      # score is now 8
    score = 2 ** 4      # score is now 16
    score = 2 ** 5      # score is now 32
    
    print(score)        # Output: 32
    

Let's give it a try!

## [#](https://www.codedex.io/python/08-bmi#instructions) Instructions

The [body mass index (BMI)](https://en.wikipedia.org/wiki/Body_mass_index) was created by a Belgian mathematician in the 1850s and it's used by health and nutrition professionals to estimate human body fat in certain populations.

It is computed by taking an individual's weight (mass) in kilograms and dividing it by the square of their height in meters.

  

bmi\=massheight2bmi = {mass \\over height²}bmi\=height2mass​

  

Create a **bmi.py** program that calculates your own BMI.

**Author's note:** Psst. BMI is an archaic and oversimplified way to measure personal health. It was created by a mathematician — not a doctor! 💡



