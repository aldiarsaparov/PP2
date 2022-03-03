import datetime

some = datetime.datetime(2022, 3, 1)
dt = datetime.datetime.today()
result = dt - some
total_secs = result.total_seconds()
print(total_secs)
