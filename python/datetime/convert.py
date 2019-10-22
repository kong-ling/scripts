import os
import sys
import time
from datetime import datetime, timedelta, tzinfo

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
print(now)
#now_utc = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
now_utc = datetime.utcnow()
print(now_utc)
now_bj = (now_utc + timedelta(hours=8)).strftime("%Y-%m-%d_%H-%M-%S")

print(now_bj)

while True:
    nowtime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    print('%s %s' % ('\b'*20, nowtime)) #2019-03-11 13:45:54.253584
    time.sleep(1)
