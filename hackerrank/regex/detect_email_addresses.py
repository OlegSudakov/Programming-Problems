# https://www.hackerrank.com/challenges/detect-the-email-addresses

import re

pattern = r"\w+[\w.]+@[\w.]+\w+"

n = int(input())

addresses = set()

for i in range(n):
    line = input()
    addresses.update(re.findall(pattern, line))
addresses = list(addresses)
addresses.sort()
print(";".join(addresses))
