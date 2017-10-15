# https://www.hackerrank.com/challenges/hackerrank-tweets

import re

n = int(input())
pattern = r"hackerrank"
count = 0

for i in range(n):
    string = input().lower()
    if re.search(pattern, string):
        count += 1
print(count)
