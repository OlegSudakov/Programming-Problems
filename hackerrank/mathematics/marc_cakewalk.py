# https://www.hackerrank.com/challenges/marcs-cakewalk

import sys

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse = True)
mult = 1
total = 0
for cal in calories:
    total += mult*cal
    mult *= 2
print(total)
