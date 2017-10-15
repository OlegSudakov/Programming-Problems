# https://www.hackerrank.com/challenges/breaking-best-and-worst-records

import sys

def getRecord(s):
    max_r = s[0]
    min_r = s[0]
    max_c = 0
    min_c = 0
    for i in range(1, len(s)):
        if s[i] > max_r:
            max_r = s[i]
            max_c += 1
        if s[i] < min_r:
            min_r = s[i]
            min_c += 1
    return max_c, min_c

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
