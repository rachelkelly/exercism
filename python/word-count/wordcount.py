# -*- coding: utf-8 -*-
#
# Word Count exercism - Python
#

import re

def word_count(sentence):

    # Creates a list of words based on excluding all non-ascii symbols
    # and lower-cases all of the words, all in one go.
    sentlist = list(re.findall(r'[^\W_]+', sentence.lower(), flags=re.UNICODE))

    # populate or add to new dict 
    sentdict = {}
    for key in sentlist: 
        if key in sentdict:
            sentdict[key] += 1
        elif key not in sentdict:
            sentdict[key] = 1

    return sentdict
