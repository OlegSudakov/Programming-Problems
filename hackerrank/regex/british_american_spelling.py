# https://www.hackerrank.com/challenges/uk-and-us

import re

n = int(input())

strings = []
for i in range(n):
    strings.append(input())

q = int(input())
for i in range(q):
    subword = input()
    pattern = r"({}se|{}ze)".format(subword[:-2], subword[:-2])
    res = 0
    for j in range(n):
        res += len(re.findall(pattern, strings[j]))
    print(res)
