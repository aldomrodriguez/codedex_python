# 25\. Reading List

## [#](https://www.codedex.io/python/25-reading-list#list-methods) List Methods

Besides built-in functions, Python has a bunch of built-in list methods that are very handy.

Here are some of them:

-   `.append()` method adds an item to the end of the list.
-   `.insert()` method adds an item to a specific index.
-   `.remove()` method removes an item from a list based on the value.
-   `.pop()` method removes the item at a particular index.

Let's use DNA sequences as an example for this! 🧬

    dna = ['AUG', 'AUC', 'UCG']
    
    dna.append('UAA')     # ['AUG', 'AUC', 'UCG', 'UAA']
    dna.insert(2, 'GAU')  # ['AUG', 'AUC', 'GAU', 'UCG', 'UAA']
    dna.remove('AUC')     # ['AUG', 'GAU', 'UCG', 'UAA']
    dna.pop(0)            # ['GAU', 'UCG', 'UAA']
    

The difference between built-in functions and methods on a list is that methods use the dot notation syntax on the list variable we create. Built-in functions can be called by themselves, but methods are always attached to a list variable from which they are being called.

Another notable difference is that while not all the built-in functions are defined to work with lists, the list methods only work with lists.

Here are all 11 list methods to save in your notes:

| List Method   | Description |
|--------------|------------|
| `.append()`  | Add an item to the end of the list |
| `.clear()`   | Remove all items from the list |
| `.copy()`    | Return a shallow copy of the list |
| `.count()`   | Return the number of times the value appears in the list |
| `.extend()`  | Appends another list to the current list by extending it |
| `.index()`   | Returns the index of a value inside the list |
| `.insert()`  | Insert an item at a specified position in the list |
| `.pop()`     | Remove an item from a specified position in the list |
| `.remove()`  | Remove an item from the list based on the value of the item |
| `.reverse()` | Reverses the list in place |
| `.sort()`    | Sorts the list in place |

Sorts the list in place

## [#](https://www.codedex.io/python/25-reading-list#instructions) Instructions

Let's start a book club by making a list of popular books! 📚

Create a **reading\_list.py** program that stores the following items in a `books` list:

-   `'Harry Potter'`
-   `'1984'`
-   `'The Fault in Our Stars'`
-   `'The Mom Test'`
-   `'Life in Code'`

Suppose we want to add `'Pachinko'` to the list. Can you use a list method to do so?

Let's say we finished reading `'The Fault in Our Stars'` and `'1984'`. Can you use the `.remove()` method to remove one and the `.pop()` method to remove the other?

Print the updated list out to make sure everything's good to go!



