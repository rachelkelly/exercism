# Python "Bob" exercism exercise

def hey(what):
    what = what.strip() # to eliminate -foolishness- whitespace
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

