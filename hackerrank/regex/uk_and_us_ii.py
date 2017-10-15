# https://www.hackerrank.com/challenges/uk-and-us-2

import re

n = int(input())

strings = []
for i in range(n):
    strings.append(input())

q = int(input())
for i in range(q):
    subword = input()
    subword_2 = subword.replace("our", "or")
    pattern_1 = r"((?<=\s){}(?=\s)|^{}(?=\s)|(?<=\s){}$)".format(subword, subword, subword)
    pattern_2 = r"((?<=\s){}(?=\s)|^{}(?=\s)|(?<=\s){}$)".format(subword_2, subword_2, subword_2)
    res = 0
    for j in range(n):
        res += len(re.findall(pattern_1, strings[j]))
        res += len(re.findall(pattern_2, strings[j]))
    print(res)
