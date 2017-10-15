# https://www.hackerrank.com/challenges/2d-array

import sys

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
max_sum = None
for j in range(6-2):
    for i in range(6-2):
        s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if max_sum is None:
            max_sum = s
        elif s > max_sum:
            max_sum = s
print(max_sum)
