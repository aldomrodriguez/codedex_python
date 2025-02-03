# 13\. pH Levels

## [#](https://www.codedex.io/python/13-ph-levels#relational-operators) Relational Operators

A lot of the times inside conditions, we are comparing two values. To do so, we need to use a different type of operators called **relational operators** that compares values:

-   `==` equal to
-   `!=` not equal to
-   `>` greater than
-   `<` less than
-   `>=` greater than or equal to
-   `<=` less than or equal to

## [#](https://www.codedex.io/python/13-ph-levels#elif) Elif

One or more `elif` statements (short for "else if") can be optionally added in between the `if` and `else` to provide additional condition(s) to check. Sometimes two is simply not enough.

    if grade > 90:
      print('A')
    elif grade > 80:
      print('B')
    elif grade > 70:
      print('C')
    elif grade > 60:
      print('D')
    else:
      print('F')
    

**Note:** Only one of these options will execute.

## [#](https://www.codedex.io/python/13-ph-levels#instructions) Instructions

In chemistry, [pH](https://en.wikipedia.org/wiki/PH) is a scale used to specify the acidity or basicity of a liquid. 🧪

Create a **ph\_levels.py** program that checks whether a pH level is basic, acidic, or neutral.

First, create a `ph` variable and ask the user for a value between 0 and 14.

Write an `if`, `elif`, `else` statement that:

-   If `ph` is greater than 7, output "Basic".
-   If `ph` is less than 7, output "Acidic".
-   Else, output "Neutral".



