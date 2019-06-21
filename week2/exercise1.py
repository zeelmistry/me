"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this is a variable which defines a list with text inside
some_words = ['what', 'does', 'this', 'line', 'do', '?']

#I think this will print all the words from some_words in a line 
for word in some_words:
    print(word) #it printed the words not in a line but down the page

#I think this will do the same as before, it will print the words in a line
for x in some_words:
    print(x) #it printed the words not in a line but down the page

#I think this will print the entire list which was defined earlier
print(some_words) #it did print the list with the square brackets

#I think this will print 'some_words contains more than 3 words' because some_words has more than 3 inputs
if len(some_words) > 3:
    print('some_words contains more than 3 words') #it did print 'some_words contains more than 3 words'

#Since researching uname, this function I think will display the information about the computer I am using
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    print(platform.uname()) #it did show what the current machine is running on and other information

usefulFunction()
