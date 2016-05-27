# DNA to RNA transcription

def to_rna(code):
    stringy = ''
    for i in code:
        if (i == 'G'):
            stringy = stringy + 'C'
        elif (i == 'C'):
            stringy = stringy + 'G'
        elif (i == 'T'):
            stringy = stringy + 'A'
        elif (i == 'A'):
            stringy = stringy + 'U'
