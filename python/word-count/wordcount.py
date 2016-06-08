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
    print sentlist

    # populate or add to new dict
    sentdict = {}
    for key in sentlist: # iterate over every key in dict - "key" is just an iterator to keep consistent
        if key in sentdict: # if we've seen this key before, iterate up its value
            sentdict[key] = 2
            #for key, j in sentdict.iteritems(key, j):
            #    sentdict.update(key=(j+1))
            #for i in key[i]: # not sure about this syntax
            #    j = i + 1              # make a quick new var to plug in
            #    sentdict.update(key=j) # or sentdict[key] = j ?
            #sentdict.update(key=(value+=1))
            # increment value by 1
            #pass
        else: # else condition only happens if it's the first time the word's been seen
            key.lower()
            sentdict[key] = 1 # should only happen once
            sentdict.viewitems()
        # if/else conditional happens for each word

    # return count
    return sentdict

word_count('The kids are okay kids.')
