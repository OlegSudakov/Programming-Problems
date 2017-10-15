# https://www.hackerrank.com/challenges/apple-and-orange

import sys

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]
apples = sum([1 for ap in apple if s <= a + ap <= t])
oranges = sum([1 for oran in orange if s <= oran + b <= t])

print(apples)
print(oranges)
