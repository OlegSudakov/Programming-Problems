# https://www.hackerrank.com/challenges/time-conversion

import sys
import re

pattern = r"^(\d\d):(\d\d):(\d\d)(\w\w)$"

def timeConversion(s):
    match = re.search(pattern, s)
    hour = match.group(1)
    minutes = match.group(2)
    seconds = match.group(3)
    half = match.group(4)
    if hour != "12" and half == "PM":
        hour = str(int(hour)+12)
    if hour == "12" and half == "AM":
        hour = "00"
    return "{}:{}:{}".format(hour, minutes, seconds)
    

s = input().strip()
result = timeConversion(s)
print(result)
