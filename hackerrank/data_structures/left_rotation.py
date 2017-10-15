# https://www.hackerrank.com/challenges/array-left-rotation

row = input()
n, d = row.split(" ")
n, d = [int(n), int(d)]
arr = str.split(input(), " ")
d = d % n
arr = arr[d:] + arr[0:d]
print(" ".join(arr))
