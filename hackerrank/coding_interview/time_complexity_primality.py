# https://www.hackerrank.com/challenges/ctci-big-o

import math

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    flag = True
    if n == 1:
        print("Not prime")
        continue
    for k in range(2, round(math.sqrt(n))+3):
        if n % k == 0 and k != n:
            flag = False
            print("Not prime")
            break
    if flag:
        print("Prime")

