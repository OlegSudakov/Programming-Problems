# https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude

import re

n = int(input())

x_pattern = r"^[+-]?(90(\.0+)?|([1-8][0-9]|[1-9])(\.[0-9]+)?)$"
y_pattern = r"^[+-]?((1[0-7][0-9]|[1-9][0-9]|[1-9])(\.[0-9]+)?|180(\.0+)?)$"

for i in range(n):
    x, y = input().split(", ")
    x = x[1:]
    y = y[:-1]
    if re.match(x_pattern, x) and re.match(y_pattern, y):
        print("Valid")
    else:
        print("Invalid")
