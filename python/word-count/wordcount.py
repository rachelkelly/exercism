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
    for key in sentlist: # key is just iterator to be consistent throughout conditional
        if key in sentdict: # if we've seen this key before, increment its value
            sentdict[key] = 2 # this will only work once
            #for key, value in sentdict.iteritems():
            #    value += 1 # this is NOT currently incrementing the value
            print "repeat"
        else:
            sentdict[key] = 1
        print sentdict

    # return count
    return sentdict

# just for my own testing
word_count('The the the kids are okay kids')
