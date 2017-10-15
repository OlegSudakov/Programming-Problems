# https://www.hackerrank.com/challenges/find-substring

import re

n = int(input())

strings = []
for i in range(n):
    strings.append(input())

q = int(input())
for i in range(q):
    subword = input()
    pattern = r"(\w)+{}(\w)+".format(subword)
    res = 0
    for j in range(n):
        res += len(re.findall(pattern, strings[j]))
    print(res)
