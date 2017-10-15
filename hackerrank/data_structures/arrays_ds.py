# https://www.hackerrank.com/challenges/arrays-ds

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

l = []
for i in arr:
    l.insert(0, str(i))
print(" ".join(l))
