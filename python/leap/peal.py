# Write a program that will take a year and report if it is a leap year.
#
# On every year div by 4
#  unless year div by 100
#    unless year div by 400, in which case ok!

def leapy(year=0):
    if (year % 400 == 0):
        print "yes"
    elif (year % 100 == 0):
        print "no"
    elif (year % 4 == 0):
        print "yes"
    else:
        print "no"

#leapy()
