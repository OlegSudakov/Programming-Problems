# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

import sys

def minimumAbsoluteDifference(n, arr):
    min_dist = abs(arr[1] - arr[0])
    arr.sort()
    for i in range(2, len(arr)):
        if abs(arr[i] - arr[i-1]) < min_dist:
            min_dist = abs(arr[i] - arr[i-1])
    return min_dist
        

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
