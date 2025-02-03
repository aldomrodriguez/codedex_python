Exercise

# 19\. Detention

## [#](https://www.codedex.io/python/19-detention#range) range()

To loop through a set of code a specified number of times, we can use a `for` loop and the `range()` function.

The `range()` function returns a sequence of numbers. By default, the sequence starts at 0 and increments by 1, ending at a specified number.

    for i in range(6):
      print(i)
    

For number `i` inside `range(6)`, which is 0 through 5, print number `i`.

This will output:

    0
    1
    2
    3
    4
    5
    

Notice how this stops at 5, and 6 is not printed. This is because `range()` actually ends one before the specified number.

## [#](https://www.codedex.io/python/19-detention#instructions) Instructions

![detention](https://www.codedex.io/images/detention.png)

Suppose you got detention and the teacher wants you to write "I will not use Snapchat in class" on the whiteboard 100 times.

Create a **detention.py** program that does this using code.

(This is where we begin to see the true power of computing. What takes humans hours can take a computer microseconds. 🤯)



