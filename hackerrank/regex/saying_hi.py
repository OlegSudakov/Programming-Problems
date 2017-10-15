# https://www.hackerrank.com/challenges/saying-hi

import re

pattern = r"^[Hh][Ii]\s[^dD]"

n = int(input())

for i in range(n):
    string = input()
    if re.match(pattern, string):
        print(string)
