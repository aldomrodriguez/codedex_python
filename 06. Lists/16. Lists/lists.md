Exercise

# 22\. Grocery List

## [#](https://www.codedex.io/python/22-grocery#lists) Lists

Welcome to the Lists chapter! Thank you for sticking around. :)

Here, we'll learn about a neat way to store a bunch of data values. 📦 = ⚽️🏀⚾️🥎🏐🏈

![](https://i.imgur.com/WVloHi6.gif)

Suppose we want to build a program that stores student grades for homework and quizzes, we would need to create a bunch of variables like so:

    # Storing grades in a class
    
    hw_grade1 = 98
    hw_grade2 = 87
    hw_grade3 = 92
    hw_grade4 = 96
    
    quiz_grade1 = 9
    quiz_grade2 = 6
    quiz_grade3 = 8
    

Creating a bunch of variables this way is tedious and error-prone. Can you imagine what it would be like with 100+ students?

Lists are used to store multiple items in a single variable.

We can rewrite the above code to:

    # Storing grades in a class
    
    hw_grades = [98, 87, 92, 96]
    quiz_grades = [9, 6, 8]
    

The syntax for a list looks like:

    list_name = [item1, item2, item3, item4]
    

Lists are created using square brackets `[` and `]`. And the items are separated by `,` commas.

## [#](https://www.codedex.io/python/22-grocery#examples) Examples

Data that could be stored in a list:

-   Temperatures in the past week.
-   pH level of the office plant in the past hour.
-   "Now playing" in the movie theater nearby.

    temp = [86, 80, 82, 87, 79, 80, 82]
    ph = [7.2, 7.1, 7.0, 7.0, 7.2, 7.1]
    now_playing = ['Barbie', 'Oppenheimer', 'Talk to Me', 'Blue Beetle']
    

More facts about lists:

-   List items allow duplicate values.
-   Lists can have values with different data types.
-   There's no limit to how much data a list can hold.

## [#](https://www.codedex.io/python/22-grocery#instructions) Instructions

Create a **grocery.py** program with a `grocery` list of things that you need from the store:

-   `'🥚 Eggs'`
-   `'🥑 Avocados'`
-   `'🍪 Cookies'`
-   `'🌶 Hot Pepper Jam'`
-   `'🫐 Blueberries'`
-   `'🥦 Broccoli'`

Print out `grocery` to make sure you got it!



