#
# Gigasecond exercism - Python
#

import datetime

# time_of_birth is a 5-parameter variable
def add_gigasecond(time_of_birth):
    print 'Date of Birth including time:', time_of_birth
    gs = datetime.timedelta(seconds=1000000000)
    gs_day = time_of_birth + gs
    return gs_day #always return from a func
