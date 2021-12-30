import datetime

start = datetime.datetime(1901, 1, 1)
counter = 0
while start <= datetime.datetime(2000, 12, 31):
  if int(start.strftime("%d")) == 1 and start.weekday() == 6:
    print(start, int(start.strftime("%d")), start.weekday())
    counter += 1
  start = start + datetime.timedelta(days=1)
print()
print(counter)