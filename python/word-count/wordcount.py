# -*- coding: utf-8 -*-

#
# Word Count exercism - Python
#

# Create list of incoming sentence with a for loop list append
# Create empty dict.  For each new word add key to dict with value 1.
 # if word already in dict, integer++ for dict item value
# for each word, return a count

def word_count(sentence):
    
    # turn the sent into a list for parsing
    sentlist = []
    for i in sentence:
        sentlist.append(i)

    # populate or add to new dict
    sentdict = {}
    for key in sentlist: # iterate over every key in dict
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
            sentdict[key] = 1 # should only happen once
            sentdict.viewitems()
        # if/else conditional happens for each word

    # return count
    for key in sentdict:
        pass        

word_count('The kids are okay kids.')
