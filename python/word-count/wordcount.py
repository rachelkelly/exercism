# -*- coding: utf-8 -*-

#
# Word Count exercism - Python
#

from string import split

def word_count(sentence):

    for i in sentence:
        if i in ("\"\\'!@#$%^&*():;,.[]|{}-_=+`~?"):
            sentence.replace(sentence[i], ' ')

# oof below
#    sentenceprocessing = list(sentence)
#    for i in sentenceprocessing:
#        if i in ("\"\\'!@#$%^&*():;,.[]|{}-_=+`~?"):
#            sentenceprocessing[i] = " "
#    sentence = "".join(sentenceprocessing)    
#    for i in sentence:
#        if i in ("\"\\'!@#$%^&*():;,.[]|{}-_=+`~?"):
#            print i
#            i = " "
    sentlist = split(sentence.lower())

    # populate or add to new dict - create the empty dict, analyze each element 
    # in sentlist, ++ value if seen more than once
    sentdict = {}
    for key in sentlist: 
        if key in sentdict:
            sentdict[key] += 1
        elif key not in sentdict:
            sentdict[key] = 1

    # return count
    return sentdict

# just for my own testing
#word_count('The the the kids are okay kids.')
