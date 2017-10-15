# https://www.hackerrank.com/challenges/find-a-word

import re

pattern = r"((?<=\W){}(?=\W)|^{}(?=\W)|(?<=\W){}$)"

n = int(input())
strings = []

for i in range(n):
    strings.append(input())
    
t = int(input())

for i in range(t):
    word = input()
    count = 0
    pattern_current = pattern.format(word, word, word)
    for j in range(n):
        count += len(re.findall(pattern_current, strings[j]))
    print(count)
