#
# Gigasecond exercism - Python
#

import datetime

#where yob = year of birth, mob = month of birth, & dob = day of month of birth
def add_gigasecond(yob, mob, dob):
    DOB = datetime.date(yob, mob, dob)
    print 'Date of Birth:', DOB
    gs = datetime.timedelta(seconds=1000000000)
    gs_day = DOB + gs
    print 'Date of Gigaseconds on this planet:', gs_day
