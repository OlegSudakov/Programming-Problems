# https://www.hackerrank.com/challenges/detect-the-domain-name

import re

domains = set()

pattern = r"(http|https)://(www\.|ww2\.)?([a-zA-Z\d\.-]+\.[a-zA-Z]+)[\W_]"

n = int(input())
for i in range(n):
    line = input()
    for match in re.finditer(pattern, line):
        domains.add(match.group(3))
domains = list(domains)
domains.sort()
print(";".join(domains))
