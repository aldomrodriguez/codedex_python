Exercise

# 41\. Countdown

## [#](https://www.codedex.io/python/41-countdown#create-your-own-module) Create Your Own Module

As discussed in a previous exercise, modules are essentially **.py** files that contain statements and definitions. So all of the files that were created for the exercises up to this point could be imported as a module!

For example, recall the math functions defined in a [previous exercise](https://www.codedex.io/python/31-calculator).

If saved in a file called **calculator.py**, we could import it in a new file like so:

    import calculator
    

Suppose we have another file called **main.py**, the functions from **calculator.py** (`add()`, `subtract()`, etc.) can be accessed and used with dot notation like so:

    import calculator
    import datetime
    
    calculator.add(3, 4)        # 7
    calculator.subtract(3, 4)   # -1
    calculator.multiply(3, 4)   # 12
    calculator.divide(3, 4)     # 0.75
    calculator.exp(3, 4)        # 27
    

**Note:** The two files need to be in the same folder.

## [#](https://www.codedex.io/python/41-countdown#datetime-module) datetime Module

Wait, what was _that_ module? No, not `calculator`, the other one...

The [`datetime`](https://docs.python.org/3/library/datetime.html) module specializes in dates and times. Just like `random`, it comes with Python by default and can simply be imported.

In addition to functions, modules may contain class object definitions with their own defined methods and properties.

The `datetime` module has a `date` object that accepts the following properties:

-   `.year`: An integer between 1 and 9999.
-   `.month`: An integer between 1 and 12.
-   `.day`: An integer between 1 and the number of days in a given month.

The syntax for a `date` is `datetime.date(year, month, day)`, like so:

    import datetime
    
    release_date = datetime.date(1991, 2, 20)
    print(release_date)     # Output: 1991-02-20
    

The output shows the `date` object with a dash between each part. Also, any single number gets a leading zero `0`.

The `.year`, `.month`, and `.day` properties can be accessed like with any other class object:

    print(f'Python was released in {release_date.year}.')
    # Output: Python was released in 1991.
    

Retrieving the current date is possible with the `date.today()` method:

    datetime.date.today()
    

## [#](https://www.codedex.io/python/41-countdown#instructions) Instructions

Let's use the `datetime` and `random` modules to make a [birthday card](https://en.wikipedia.org/wiki/Birthday_card) to determine how far your birthday is from today! 🎂

For this exercise, we are creating _two_ **.py** files in a separate code editor.

**Note:** You can do this on VS Code! Check out [this article](https://www.codedex.io/projects/set-up-your-local-environment-in-python) to set up VS Code.

### [##](https://www.codedex.io/python/41-countdown#bday_messagespy) bday\_messages.py

Create a new file called **bday\_messages.py**.

Import the `random` module.

Then, define a `bday_messages` list with the following items:

-   'Hope you have a very Happy Birthday! 🎈',
-   'It's your special day – get out there and celebrate! 🎉',
-   'You were born and the world got better – everybody wins! 🥳',
-   'Have lots of fun on your special day! 🎂',
-   'Another year of you going around the sun! 🌞'

Next, use the `random.choice()` method to get a single item from the list.

Save this item in a `random_message` variable.

Let's save **bday\_messages.py** and move to the next part.

### [##](https://www.codedex.io/python/41-countdown#mainpy) main.py

Create a new file called **main.py**.

Import both the `datetime` module as well as `bday_messages` (the last file).

    import datetime, bday_messages
    

Next, use the `datetime` module to create two `date` objects:

-   `today`: Today's date, using the `datetime.date.today()` method.
-   `next_birthday`: The date for your **next** birthday, using the `year`, `month`, and `day` arguments.

A really cool thing you can do with `date` objects is addition and subtraction!

    time_difference = date1 - date2
    

Use date subtraction to calculate how many days away `today` is from `next_birthday`. Then, assign the result to a new variable called `days_away`.

Then, create a control flow statement:

-   If `today` is equal to `next_birthday`, print the `random_message` variable (imported from `bday_messages`).
-   Else, print `'My next birthday is {days_away} days away!'`.

The output should look something like this:

    My next birthday is 42 days away!
    

**Bonus:** Instead of using a date in the future, what if we tried to see how many days it's been since a _past_ event, like the release date of your favorite movie or game, or the date you were born? What about how many years or months it's been?



