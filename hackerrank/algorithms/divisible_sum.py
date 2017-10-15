# https://www.hackerrank.com/challenges/divisible-sum-pairs

import sys

def divisibleSumPairs(n, k, ar):
    count = 0
    for j in range(1, len(ar)):
        for i in range(0, j):
            xi = ar[i]; xj = ar[j]
            if (xi + xj) % k == 0:
                count += 1
    return count
            

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
result = divisibleSumPairs(n, k, ar)
print(result)
