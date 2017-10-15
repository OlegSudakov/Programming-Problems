# https://www.hackerrank.com/challenges/ide-identifying-comments

import re

pattern = r"(\/\/.*|/\*+[^/*]+\*+\/)"

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break
code = "\n".join(lines)
for match in re.findall(pattern, code):
    for line in match.split("\n"):
        line = str.lstrip(line)
        print(line)
