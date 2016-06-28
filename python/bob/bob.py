# Python "Bob" exercism exercise

import string

def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    elif "Let's" in what:
        return 'Whatever.'
    elif '!' in what:
        return 'Whoa, chill out!'
    elif what == '':
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'

