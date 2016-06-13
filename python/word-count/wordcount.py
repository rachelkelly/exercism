# -*- coding: utf-8 -*-

#
# Word Count exercism - Python
#

# ! DONE # Create list of incoming sentence with a for loop list append
# ! DONE # Create empty dict.  For each new word add key to dict with value 1.
 # if word already in dict, integer++ for dict item value
# for each word, return a count
# ! DONE # account for case too!
# ! DONE # gotta put WORDS into the list, not letters.

# need to import the string lib?
from string import split

def word_count(sentence):
    
    # turn the sent into a list for parsing
    sentlist = split(sentence.lower()) # split sentence into distinct words & lowercase them all

    # populate or add to new dict - create the empty dict, analyze each element 
    # in sentlist, ++ value if seen more than once
    sentdict = {}
    for key in sentlist: # key is just iterator to be consistent throughout conditional
        if key in sentdict: # if we've seen this key before, increment its value
            sentdict[key] = 2 # need to generically refer to its value in order to increment value
        else:
            sentdict[key] = 1

    # return count
    return sentdict

# just for my own testing
word_count('The kids are okay kids.')
