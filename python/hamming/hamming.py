# Hamming distance calculator

def distance(strand1, strand2):
    if len(strand1) != len(strand2):
        pass
    else:
        thirdline = '' # creates empty string in which to indicate match or no-match
        strandlength = len(strand1) # bc first conditional passed we know length of two strands is same
        while strandlength > 0:
            if strand1[i] == strand2[j]: # NOPE:  next try 'for i in strand1' to populate a list & compare over list iterations
                thirdline = thirdline + ' '
            else:
                thirdline = thirdline + '^'
            strandlength -= 1

#        for i in strand1:
#            for j in strand2: # what I really wanted was "for i in strand1 and for j in strand2: " but that threw an error
#                if i == j:
#                    thirdline = thirdline + ' '
#                else:
#                    thirdline = thirdline + '^'
#                    print thirdline
#                break
    diff = 0
    for k in thirdline:
        if k == '^':
            diff =+ 1
        print strand1
        print strand2
        print thirdline
        print "The Hamming distance between these DNA strands is %d." %diff

distance('GCA', 'GCG')


