# Number guessing
Demo solution can be found on the “demo_solution” branch.

### Source: https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

### Technology
- Python 3.7

## Introduction
The program will first randomly generate a number unknown to the user. The user needs to guess what that number is. (In other words, the user needs to be able to input information in several times.) If the user’s guess is wrong, the program should return some sort of indication as to how wrong (first of all the guessed number is too high or too low, second the guessed number's characters are appear in the random number and if they, is their place is right or not). If the user guesses correctly, a positive indication should appear. 

## Example
```
Hello, My Dear Friend! I randomly generated a number between 0 and 100000. 
Can you find out?

Give me a guess, please!
4 //input

Your guess is smaller than my number.
The 4 is in my number somewhere.
And in the right place.

Give me a guess, please!
6532 //input

Your guess is smaller than my number.
The 3 is in my number somewhere.
And in the right place.
The 2 is in my number somewhere.
But in the wrong place.
```

## Extras
You can implement a restart option into the game after the succesfull guess. 
