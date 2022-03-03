from datetime import datetime, timedelta

present = datetime.now()
yesterday = present - timedelta(1)
tomorrow = present + timedelta(1)

print("Yesterday was", yesterday)
print("Today is", present)
print("Tomorrow is ", tomorrow)


