# 38\. Pokédex

## [#](https://www.codedex.io/python/38-pokedex#congrats) Congrats!

Nice! You've reached the end of another chapter! 🥳

Let's recap what we learned:

We learned how to:

-   Create a class and initialize them with certain attributes.
-   Create objects based on these classes and set values for these attributes.
-   Create classes using the special `__init__()` method.
-   Create instance methods that will update or use these class attributes.

Check out the `Student` class definition for a refresher:

    class Student:
      def __init__(self, name, year, enrolled, gpa):
        self.name = name
        self.year = year
        self.enrolled = enrolled
        self.gpa = gpa
    
      def display_info(self):
        print('The student ' + self.name + '\'s GPA is ' + self.gpa + '!')
    
      def graduation(self):
        if self.enrolled and self.gpa > 2.5 and self.year == 12:
          print(self.name + ' will be able to graduate this year!')
    

In this final exercise, we will build a fun project using everything we've learned about classes and objects!

Let's get started!

## [#](https://www.codedex.io/python/38-pokedex#instructions) Instructions

Since 1996, the [Pokémon](https://en.wikipedia.org/wiki/Pok%C3%A9mon) video game franchise has delighted players around the world with collectible pocket monsters. A **Pokédex** is a device that tracks the information for Pokémon that are seen or caught.

Create a new file called **pokedex.py**.

Next, let's define a `Pokemon` class with the following attributes:

-   `entry` (integer)
-   `name` (string)
-   `types` (list of strings)
-   `description` (string)
-   `is_caught` (boolean)

**Note:** Make sure to use the `__init__()` method.

Next, create an instance method called `.speak()` that prints a string of the sound a Pokémon makes. A Pokémon usually just says their name, so make the `.speak()` simply print out their name twice!

Then, create another instance method called `.display_details()` that prints the attributes of a `Pokemon` object like the following:

    Entry Number: 25
    Name: Pikachu
    Type: Electric
    Description: It has small electric sacs on both its cheeks. If threatened, it looses electric charges from the sacs.
    Pikachu has already been caught!
    

Lastly, create three `Pokemon` class objects and use the `.speak()` or `.display_details()` instance methods for each one.

For more information about any Pokémon you want to add, see the [Pokédex](https://www.pokemon.com/us/pokedex)!

Are you ready to earn the next badge?

**Bonus:** For all the super fans, try and add more attributes to the `Pokemon` class definition, like `level`, `region`, `height`, or `weight`.



