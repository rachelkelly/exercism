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
    for key in sentlist: # iterate over every key in dict
        if key in sentdict: # if we've seen this key before, iterate up its value
            for i in get(key[, i]) # not sure about this syntax
                j = i + 1              # make a quick new var to plug in
                sentdict.update(key=j) # 
            #sentdict.update(key=(value+=1))
            # increment value by 1
            pass
        else: # else condition only happens if it's the first time the word's been seen
            sentdict[key] = 1 # should only happen once

word_count('The kids are okay kids.')
