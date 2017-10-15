# https://www.hackerrank.com/challenges/valid-pan-format

import re

pattern = r"^[A-Z]{5,5}[0-9]{4,4}[A-Z]$"

n = int(input())

for i in range(n):
    string = input()
    if re.match(pattern, string):
        print("YES")
    else:
        print("NO")
