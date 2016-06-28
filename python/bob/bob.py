#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
    if '?' in what:
        return 'Sure.'
        #print 'Sure.' # just for testing
    elif '!' in what:
        return 'Whoa, chill out!'
        #print 'Whoa, chill out!'
    else:
        return 'Whatever.'
        #print 'Whatever.'

hey('Wanna eat?')
hey('!!!')
hey('The aphrodisiac was in you all along.')
