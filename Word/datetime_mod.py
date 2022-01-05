import datetime
import time

print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()))
print(time.ctime())

dt = datetime.datetime(2020, 12, 23, 4, 12, 3)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)

print(datetime.datetime.fromtimestamp(1000000))

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds)
print(delta.total_seconds())

print(5)
print("the time now", datetime.datetime.now())
print(type(dt))
