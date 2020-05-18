import datetime
import os
import time

now = datetime.datetime.now()


x=int(input("Enter the hour in 24 hour format: "))
y=int(input("Enter the minutes: "))

print("The alarm is set for",x, "hours", y, "minutes")

alarm_time = datetime.datetime.combine(now.date(), datetime.time(x, y, 0))

time.sleep((alarm_time - now).total_seconds())

os.system("start 01.En_Frienda_Pola.mp3")