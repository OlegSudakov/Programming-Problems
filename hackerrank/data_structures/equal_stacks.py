# https://www.hackerrank.com/challenges/equal-stacks

import sys
from itertools import accumulate

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1 = h1[::-1]; h2 = h2[::-1]; h3 = h3[::-1]
acc_1 = set(accumulate(h1)); acc_2 = set(accumulate(h2)); acc_3 = set(accumulate(h3))

h_max = 0
for h in acc_1:
    if h in acc_2 and h in acc_3:
        if h > h_max:
            h_max = h
            
print(h_max)
