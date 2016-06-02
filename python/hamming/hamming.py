# Hamming distance calculator

def distance(strand1, strand2):
    hamcount = 0

    for i, item in enumerate(strand1):
        if strand1[i] == strand2[i]:
            pass
        else:
            strand1[i] != strand2[i]
            hamcount += 1
    return hamcount
