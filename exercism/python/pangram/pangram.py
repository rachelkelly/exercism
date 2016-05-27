# exercism: pangram
import sys

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_pangram(phrase):
    for i in phrase:
        if i in alphabet:
            print "ok, removing %s" %i
            alphabet.remove(i)
    if not alphabet: # == if alphabet is empty
        return True
