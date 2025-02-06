# Checkpoint Project ⛳️

Congratulations on completing the first four chapters of The Legend of Python! Now let's use the skills you've learned (variables, control flow statements, and loops) to build a Python project on your own.

Use the [Python Code Editor](https://www.codedex.io/editor/python), [Visual Studio Code](https://code.visualstudio.com/), or your code editor of choice for this project.

## [#](https://www.codedex.io/python/checkpoint-project/rock-paper-scissors#rock-paper-scissors) Rock Paper Scissors

[Rock, Paper, Scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) is a classic game that resonates with folks from around the world.

Create a **rock\_paper\_scissors.py** program where the user plays a round of Rock, Paper, Scissors with the computer.

The rules are as follows:

-   Rock beats Scissors.
-   Scissors beat Paper.
-   Paper beats Rock.

First, create a `player` and a `computer` variable.

Prompt the player to select number between 1 and 3 with `input()` and store it in `player`:

-   `1` is for `“✊”` (Rock).
-   `2` is for `“✋”` (Paper).
-   `3` is for `“✌”` (Scissors).

Then, use the `random.randint()` method to assign a number to the `computer` variable (1 to 3).

Lastly, use control flow to compare the user's choice and the computer's choice, determine the winner, and print out who won.

The output should look something like this:

    ===================
    Rock Paper Scissors
    ===================
    1) ✊
    2) ✋
    3) ✌️
    Pick a number: 2
    
    You chose: ✋
    CPU chose: ✊
    The player won!
    

## [#](https://www.codedex.io/python/checkpoint-project/rock-paper-scissors#bonus-rock-paper-scissors-lizard-spock) Bonus: Rock Paper Scissors Lizard Spock

Okay, you have played Rock, Paper, Scissors, but have you heard of [Rock, Paper, Scissors, Lizard, Spock](https://www.youtube.com/watch?v=iSHPVCBsnLw)? It's a fun variation of the classic game brought to popularity with a TV show called _The Big Bang Theory_.

The rules are very similar to the ones from the classic “Rock Paper Scissors” but with two new options, “Lizard” and “Spock”:

-   Scissors cut Paper.
-   Paper covers Rock.
-   Rock crushes Lizard.
-   Lizard poisons Spock.
-   Spock smashes Scissors.
-   Scissors beat Lizard.
-   Lizard eats Paper.
-   Paper disproves Spock.
-   Spock vaporizes Rock.
-   Rock breaks Scissors.

Watch [this video](https://www.youtube.com/watch?v=iSHPVCBsnLw) to understand it better.

Here's a note from the creator, Sam Kass:

> _“I invented this game (with Karen Bryla) because it seems like when you know someone well enough, 75-80% of any Rock Paper Scissors games you play with that person end up in a tie. Well, here is a slight variation that reduces that probability. This version is also nice because it satisfies the Law of Fives.”_

Go back to your Rock Paper Scissors program and see if you can turn it into Rock Paper Scissors Lizard Spock!

Use `"🖖"` for "Spock and `"🦎"` for "Lizard".

The output should look something like this:

    ================================
    Rock Paper Scissors Lizard Spock
    ================================
    1) ✊
    2) ✋
    3) ✌️
    4) 🦎
    5) 🖖
    Pick a number: 3
    
    You chose: ✌️
    CPU chose: ✌️
    It's a tie!


