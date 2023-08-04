# today.py

from datetime import *

today = datetime.today()
print("\nToday is:", today, "\n")

for attribute in ["year", "month", "day", "hour", "minute", "second", "microsecond"]:
    print(attribute, ":\t", getattr(today, attribute))

print("\nTime: ", today.hour, ":", today.minute, sep = "")

day = today.strftime('%A')
month = today.strftime('%B')

print("Date:", day, month, today.day, "\n")
