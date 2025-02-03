Exercise

# 17\. Enter PIN

## [#](https://www.codedex.io/python/17-enter-pin#loop) Loop

In programming, a **loop** is used to repeat a block of code until a specified condition is satisfied. It's another incredibly powerful tool that's used a ton!

People will often use the generic term “iterate” when referring to loops; iterate simply means “to repeat”.

The first kind of loop that we are going to learn is the `while` loop. You can think of the `while` loop like a traffic circle.

Each lap is one iteration! A car will iterate over and over again until it can't do so anymore.

![roundabout example](https://www.codedex.io/images/roundabout.gif)

## [#](https://www.codedex.io/python/17-enter-pin#instructions) Instructions

Before we dive deep into `while` loop, let's see a demo using a bank's ATM. 🏦

Create an **enter\_pin.py** program and type in the following:

    print('BANK OF CODÉDEX')
    
    pin = int(input('Enter your PIN: '))
    
    while pin != 1234:
      pin = int(input('Incorrect PIN. Enter your PIN again: '))
    
    if pin == 1234:
      print('PIN accepted!')
    

Next, press the "Run" button to see the messages print to the terminal.

Try the following in the terminal on the right 👉:

1.  Type 1111 and then the enter key.
2.  Type 2023 and then the enter key.
3.  Type 1991 and then the enter key.
4.  Type 1234 and then the enter key.

Were you able to get access to the ATM?



