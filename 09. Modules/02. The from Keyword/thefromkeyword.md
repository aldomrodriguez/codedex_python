# 40\. Solar System

## [#](https://www.codedex.io/python/40-solar-system#the-from-keyword) The `from` Keyword

What if we wanted to import a piece of a module instead of the whole thing? We can use the `from` keyword!

At the top of our file, this keyword goes _before_ the `import` keyword:

    from module_name import objects
    

We can use the `from` keyword to import one or more objects from a module, such as built-in classes, methods, or variables.

The next example uses the `from` keyword to import `random` module's `.sample()` method that returns a list of values randomly picked from another list:

    from random import sample
    
    famous_houses = [
      '🐺 Stark',
      '🐉 Targaryen',
      '🦌 Baratheon',
      '🦑 Greyjoy',
      '🦁 Lannister'
    ]
    
    example = sample(famous_houses, 2)
    
    print(f'Example: {example}')
    

Since the `.sample()` method was directly imported, we can just write `sample()` instead of the usual `random.sample()`.

By the way, more than one method, variable, or class can be imported from a module on a single line.

If we want to import both the `.choice()` and `.sample()` methods:

    from random import choice, sample
    

**Note:** The `random.choice()` method randomly selects and returns a single element from a list.

## [#](https://www.codedex.io/python/40-solar-system#the-as-keyword) The `as` Keyword

Some module names are long, and it can be unpleasant to write the word repeatedly. This is where aliasing can be helpful!

We can nickname a module by using the `as` keyword. This is called **aliasing**.

For example:

    import random as rd
    

Here, we are renaming the `random` module with a shorthand, `rd`.

From this point of the program, the `random` module will be known as `rd`.

The `from` and `as` keywords can also be combined:

    from random import sample as samp
    
    example = samp(['Stark', 'Targaryen', 'Baratheon', 'Greyjoy', 'Lannister'], 2)
    
    print('Example: ' + example[0] + ' ' + example[1])
    

Instead of typing `sample()`, we can use the alias we assigned it to, `samp()`.

## [#](https://www.codedex.io/python/40-solar-system#instructions) Instructions

Let's put our newfound knowledge of the `from` and `as` keywords to the test by finding out the surface areas of the planets in our solar system! 🪐

Create a new file called **solar\_system.py**.

Next, import the following at the top of the file:

-   From the `math` module, the `pi` (π) variable.
-   From the `random` module, the `.choice()` method, renamed as `ch` for short.

Then, copy and paste the following list:

    planets = [
      'Mercury',
      'Venus',
      'Earth',
      'Mars',
      'Saturn'
    ]
    

Next, use the `ch()` method to get a random string from `planets` and assign it to a variable called `random_planet`.

And use the imported `pi` (π) variable to calculate the surface area of a sphere:

  

area\=4πr2area = 4\\pi r^2area\=4πr2

  

To do this, we'll need to know the radius `r` for a given `random_planet` (rounded to the nearest kilometer).

Write an `if`/`elif`/`else` statement and assign a value to `r` with the following in mind:

-   If `random_planet` is 'Mercury', then `r` is 2440.
-   Else, if `random_planet` is 'Venus', then `r` is 6052.
-   Else, if `random_planet` is 'Earth', then `r` is 6371.
-   Else, if `random_planet` is 'Mars', then `r` is 3390.
-   Else, if `random_planet` is 'Saturn', then `r` is 58232.
-   Else, print "Oops! An error occurred." to the console.

Lastly, calculate the area and print the name of the `random_planet` along with its area to the console.

**Bonus:** The calculated results may seem a bit long. Is there a [built-in Python function](https://docs.python.org/3/library/functions.html) that can round it?



