# 16\. Sorting Hat

## [#](https://www.codedex.io/python/16-sorting-hat#congrats) Congrats!

Here's a recap of everything we learned so far:

-   Control flow is the order in which the program's code executes.
-   `if` statement tests a condition for truth and executes the code if it's `True`.
-   `elif` clause can be added between `if` and `else`.
-   `else` executes the code if none of the above is `True`.
-   Relational operators are used to compare two values: `==`, `!=`, `>`, `>=`, `<`, `<=`.
-   Logical operators are used to combine two or more conditions: `and`, `or`, `not`.

Here's an `if`/`elif`/`else` statement in action just in case:

    if review >= 4.5:
      print('Extraordinary')
    elif review >= 4:
      print('Excellent')
    elif review >= 3:
      print('Good')
    else:
      print('Eh')
    

Now let's put all your learnings together to create your own quiz!

## [#](https://www.codedex.io/python/16-sorting-hat#instructions) Instructions

The [Sorting Hat](https://www.google.com/search?q=sorting+hat) is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

-   🦁 Gryffindor
-   🦅 Ravenclaw
-   🦡 Hufflepuff
-   🐍 Slytherin

![](https://i.imgur.com/BWViimf.gif)

Write a program that asks the user some questions with the `int()` and `input()` functions:

    Q1) Do you like Dawn or Dusk?
        1) Dawn
        2) Dusk
    

-   If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
-   Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
-   Else, output the message "Wrong input."

    Q2) When I’m dead, I want people to remember me as:
        1) The Good
        2) The Great
        3) The Wise
        4) The Bold
    

-   If the answer is 1, Hufflepuff +2.
-   Else if answer is 2, Slytherin +2.
-   Else if answer is 3, Ravenclaw +2.
-   Else if answer is 4, Gryffindor +2.
-   Else, output the message "Wrong input."

    Q3) Which kind of instrument most pleases your ear?
        1) The violin
        2) The trumpet
        3) The piano
        4) The drum
    

-   If the answer is 1, Slytherin +4.
-   Else if the answer is 2, Hufflepuff +4.
-   Else if the answer is 3, Ravenclaw +4.
-   Else if the answer is 4, Gryffindor +4.
-   Else, output "Wrong input."

Lastly, print out the score for each house.

**Bonus:** If you want to go further, see if you can figure out how to print out the house with the most points!



