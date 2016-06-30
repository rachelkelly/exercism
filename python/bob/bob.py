# Python "Bob" exercism exercise

def hey(what):
    what = what.strip() # to eliminate -foolishness- whitespace
    if what == '':
        return 'Fine. Be that way!'
    if what.isupper(): # yelling only means caps, not just a '!'
        return 'Whoa, chill out!'
    elif what.endswith('?'):
        return 'Sure.'
    else:
        return 'Whatever.'
