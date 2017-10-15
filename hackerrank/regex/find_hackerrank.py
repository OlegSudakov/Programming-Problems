# https://www.hackerrank.com/challenges/find-hackerrank

import re

pattern_1 = r"^hackerrank.+"
pattern_2 = r".+hackerrank$"
pattern_3 = r"(^hackerrank.*hackerrank$|^hackerrank$)"

n = int(input())

for i in range(n):
    string = input()
    if re.search(pattern_1, string):
        print(1)
    elif re.search(pattern_2, string):
        print(2)
    elif re.search(pattern_3, string):
        print(0)
    else:
        print(-1)
