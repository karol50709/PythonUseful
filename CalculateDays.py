import os

from datetime import datetime
from datetime import timedelta

start=datetime.now()

newdate = start + timedelta(days=5)


if (newdate.weekday()==5):
    newdate = newdate + timedelta(days=2)
elif (newdate.weekday()==6):
    newdate = newdate + timedelta(days=1)



print (newdate)
print (newdate.weekday())