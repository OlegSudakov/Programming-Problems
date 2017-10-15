# https://www.hackerrank.com/challenges/kangaroo

import sys

def kangaroo(x1, v1, x2, v2):
    if v1 != v2:
        if abs(x1 - x2) % abs(v1 - v2) == 0:
            if x2 >= x1 and v2 <= v1:
                print("YES")
                return
            elif x1 > x2 and v1 < v2:
                print("YES")
                return
    else:
        if x1 == x2:
            print("YES")
            return
    print("NO")

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
