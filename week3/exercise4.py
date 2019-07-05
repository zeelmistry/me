# -*- coding: UTF-8 -*-
"""Week 3, Exercise 4."""


import math
# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.
    
    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}
    
    This will be quite hard, especially hard if you don't have a good diagram!
    
    Use the VS Code debugging tools a lot here. It'll make understanding 
    things much easier.
    """
    tries = 0
    guess = 0

    notfound = False

    while not notfound:
        mid = int((high + low)/2)
        if mid == actual_number:
            print("You got it, it took {} tries".format(actual_number))
            notfound = True
        elif mid > actual_number:
            print("Guess Number {}:{}".format(tries + 1, mid))
            high = mid - 1
            tries = tries + 1
        else:
            print("Guess Number {}:{}".format(tries + 1, mid))
            low = mid + 1
            tries = tries + 1
    return {"guess": guess, "tries": tries}

    

if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
