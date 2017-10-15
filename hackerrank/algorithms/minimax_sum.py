# https://www.hackerrank.com/challenges/mini-max-sum

import sys

arr = list(map(int, input().strip().split(' ')))

arr.sort()
max_sum = sum(arr[1:])
min_sum = sum(arr[:-1])

print("{} {}".format(min_sum, max_sum))
