# https://www.hackerrank.com/challenges/detect-html-links

import re

pattern = r'<a href="([^"]+?)"[^>]*>(<[^/]?[^<>]+/?>)*([^<>]*)'

n = int(input())

for i in range(n):
    line = input()
    for m in re.finditer(pattern, line):
        print("{},{}".format(m.group(1), m.group(3).lstrip()))
