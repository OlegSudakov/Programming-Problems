# https://www.hackerrank.com/challenges/sock-merchant

import sys

def sockMerchant(n, ar):
    counts = {}
    for sock in ar:
        if sock in counts:
            counts[sock] += 1
        else:
            counts[sock] = 1
    pairs = 0
    for sock in counts.keys():
        pairs += counts[sock] // 2
    return pairs
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = sockMerchant(n, ar)
print(result)
