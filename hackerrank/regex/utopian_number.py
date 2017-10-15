# https://www.hackerrank.com/challenges/utopian-identification-number

import re

pattern = r"^[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}$"

n = int(input())

for i in range(n):
    string = input()
    if re.match(pattern, string):
        print("VALID")
    else:
        print("INVALID")
