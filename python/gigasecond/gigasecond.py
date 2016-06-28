#
# Gigasecond exercism - Python
#

import datetime

def add_gigasecond(time_of_birth):
    return time_of_birth + datetime.timedelta(seconds=10**9)
