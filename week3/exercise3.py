"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random

def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number 
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """
    guessed = False

    while not guessed:
        guessedNumber = str(input(message))
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber.isdigit():
            guessed = True
        else:
            print("Not a number try again")
    return int(guessedNumber)

def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    print("\nWelcome to the guessing game!")
    print("Choose a number between _ and _ ?")

    """guessedlowerbound = False
    
    while not guessedlowerbound:
        lowerBound = input("Enter a lower bound: ")
        if lowerBound.isdigit():
            print("Great")
            guessedlowerbound = True
            print("Not a number try again")"""
    
    lowerBound = not_number_rejector("Give me a lower bound: ")

    greaterthan = False

    while not greaterthan:
        upperBound = not_number_rejector("Give me a upper bound: ")
        if upperBound > lowerBound:
            greaterthan = True
        else:
            print("This is less than your lower bound, try again")

    print("OK then, pick a number between {}".format(lowerBound)) 
    print("and {}".format(upperBound))
    lowerBound = int(lowerBound)
    upperBound = int(upperBound)

    actualNumber = random.randint(lowerBound, upperBound)
    
    guessed = False
    number2 = False

    while not guessed:
        guessedNumber = not_number_rejector("Guess a number: ")
        print("You guessed {},".format(guessedNumber),)
        if guessedNumber < lowerBound:
            print("thats lower than the lower bound!")
        elif guessedNumber > upperBound:
            print("thats higher than the upper bound!")
        else:
            if guessedNumber == actualNumber:
                print("It was {}".format(actualNumber))
                guessed = True
            elif guessedNumber < actualNumber:
                print("Too small, try again :'(")
            else:
                print("Too big, try again :'(")
    return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
