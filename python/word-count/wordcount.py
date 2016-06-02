# -*- coding: utf-8 -*-

#
# Word Count exercism - Python
#

# handle utf-8
# Create list of incoming sentence with a for loop list append
# Create empty dict.  For each new word add to dict with a 1.
 # if word already in dict, integer++ for dict item value

def word_count(sentence):
    
    # turn the sent into a list for parsing
    sentlist = []
    for i in sentence:
        sentlist.append(i)

    # populate new dict
    sentdict = {}
    for key in sentlist:
        if key in sentdict:
            #sentdict.update(key=(value+=1))
            # increment value by 1
            pass
        else:
            sentdict[key] = 1
            # add new value to dict with value 1
            # append (? - wrong word) to dict
            pass

word_count('The kids are okay kids')
