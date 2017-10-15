# https://www.hackerrank.com/challenges/birthday-cake-candles

import sys

def birthdayCakeCandles(n, ar):
    max_h = max(ar)
    return sum([1 for a in ar if a == max_h])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
