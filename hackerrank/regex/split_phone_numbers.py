# https://www.hackerrank.com/challenges/split-number

import re

pattern = r"^(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})"

n = int(input())

for i in range(n):
    number = input()
    match = re.match(pattern, number)
    print("CountryCode={},LocalAreaCode={},Number={}".format(match.group(1), match.group(2), match.group(3)))
