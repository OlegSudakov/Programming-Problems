# https://www.hackerrank.com/challenges/bon-appetit

import sys

def bonAppetit(n, k, b, ar):
    brian = (sum(ar) - ar[k])/2 + ar[k]
    anna = (sum(ar) - ar[k])/2
    if b == anna:
        print("Bon Appetit")
    else:
        print(str(int(abs(b - anna))))

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
bonAppetit(n, k, b, ar)
