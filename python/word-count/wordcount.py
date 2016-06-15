# -*- coding: utf-8 -*-

#
# Word Count exercism - Python
#

from string import split

def word_count(sentence):
    
    sentlist = split(sentence.lower()) # split sentence into distinct words & lowercase them all

    # populate or add to new dict - create the empty dict, analyze each element 
    # in sentlist, ++ value if seen more than once
    sentdict = {}
    for key in sentlist: 
        if key in sentdict:
            value = sentdict[key]
            value += 1
            print "repeat"
        elif key not in sentdict:
            sentdict[key] = 1
        print sentdict

    # return count
    return sentdict

# just for my own testing
word_count('The the the kids are okay kids')
