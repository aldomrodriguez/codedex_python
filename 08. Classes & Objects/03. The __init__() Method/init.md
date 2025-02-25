# 36\. Favorite Cities

## [#](https://www.codedex.io/python/36-favorite-cities#the-__init__-method) The \_\_init\_\_() Method

Recall how we defined our `Student` class to model students:

    class Student: 
      name = ''
      year = 0
      gpa = 0.0
      enrolled = False
    
    daniel = Student()
    

However, it feels quite clunky because we need to give each attribute in the class a default or "dummy" value that doesn't actually get passed on to the objects we create.

    print(vars(daniel))
    # Output: {}
    

For example, the `daniel` object never received values from the `Student` class in the first place! We'd have to set them like so manually:

    daniel.name = 'Daniel Li'
    daniel.year = 10
    daniel.gpa = 4.0
    daniel.enrolled = True
    

Assigning a value to each attribute on a separate line is tedious; there must be an easier way! In fact, there is: we can use the `__init__()` method!

Using `__init__()` in our class definition lets us construct objects with unique attributes. When we create a new `Student()` object, we can pass in values for each attribute to **initialize** the new object, all in a single line!

So if we reformat our `Student` class with `__init__()`:

    class Student: 
      def __init__(self, name, year, gpa, enrolled):
        self.name = name
        self.year = year
        self.gpa = gpa
        self.enrolled = enrolled
    
    daniel = Student('Daniel Li', 10, 4.0, True)
    

Note that `__init__()` also uses a separate parameter called `self`. This represents the object we'll create out of `Student()`. We need to include `self` whenever we want to use `__init__()`. It's always the first parameter.

With `self`, we can move each of the previous assignments, like `daniel.name = 'Daniel Li'`, into the method and slightly rewrite it, like `self.name = name`.

Creating objects is now so much easier! If we want to create two more objects based on characters in [Lady Bird](https://en.wikipedia.org/wiki/Lady_Bird_(film)), we just have to write:

    ladybird = Student('Christine McPherson', 12, 4.0, True)
    kyle = Student('Kyle Scheible', 12, 3.4, True)
    
    print(vars(ladybird))
    print(vars(kyle))
    
    # Output: 
    # {'name': 'Christine McPherson', 'year': 12, 'gpa': 4.0, 'enrolled': True}
    # {'name': 'Kyle Scheible', 'year': 12, 'gpa': 3.4, 'enrolled': True}
    

The `__init__` might be more effort upfront, but it saves us so much time if we create hundreds or thousands of the `Student` objects.

## [#](https://www.codedex.io/python/36-favorite-cities#instructions) Instructions

Ever wonder how many people live in New York City? What about London?

Create a **favorite\_cities.py** program.

Let's make a `City` class that uses the `__init__()` method to define the following attributes:

-   `name` (string)
-   `country` (string)
-   `population` (integer rounded to the nearest thousand people)
-   `landmarks` (list of strings)

Next, create an object for your hometown and assign the attributes above.

Lastly, create another object of the city that you've always wanted to visit!

**Bonus:** Add 2-3 more attributes, like nickname, founding year, mayor, etc.