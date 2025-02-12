# 24\. Inventory

## [#](https://www.codedex.io/python/24-inventory#built-in-functions) Built-in Functions

Python comes with some built-in functions, including ones specifically for lists.

Here are some examples:

-   The `len()` function returns the total length of a list.
-   The `max()` function returns the maximum value in a list.
-   The `min()` function returns the minimum value in a list.

Suppose we have two lists that look like:

    stock1_prices = [2.52, 2.44, 2.32, 2.41, 2.51, 2.50, 2.44]
    stock2_prices = [8.36, 8.31, 8.21, 8.21, 8.25, 8.11, 8.13]
    
    print(len(stock1_prices))      # Output: 7
    print(max(stock1_prices))      # Output: 2.52
    print(min(stock2_prices))      # Output: 8.11
    

We can find a list's length, minimum, and maximum within a split second, even if the list has 1000+ items!

To learn more, here are all the [Python built-in functions](https://docs.python.org/3/library/functions.html). However, not all built-in functions are designed to work with lists!

## [#](https://www.codedex.io/python/24-inventory#instructions) Instructions

Suppose the holidays are around the corner, and the North Pole elves need your help to have thousands of LEGO toys packed up and ready for shipping.

Create a **inventory.py** program with the following list:

    lego_parts = [8980, 7323, 5343, 82700, 92232, 1203, 7319, 8903, 2328, 1279, 679, 589]
    

Each item in the list is the quantity of a colored part for a LEGO toy.

Can you figure out the following information using built-in list functions?

-   Which LEGO part are the elves running low on? Use `min()` to find out.
-   Is there a LEGO part that the elves are overstocking? Use `max()` to find out.



