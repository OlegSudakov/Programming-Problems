# https://www.hackerrank.com/challenges/alien-username

import re

pattern = r"^(_|\.)[0-9]+[a-zA-Z]*(_)?$"
n = int(input())

for i in range(n):
    string = input()
    if re.match(pattern, string) is not None:
        print("VALID")
    else:
        print("INVALID")  
