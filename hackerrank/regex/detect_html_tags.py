# https://www.hackerrank.com/challenges/detect-html-tags

import re

pattern = r"(</\s*[\w\d]+\s*>|<\s*[\w\d]+\s*)"
trantab = str.maketrans("</> ", "    ")

tag_set = set()

n = input()
for _ in range(int(n)):
    line = input()
    found_tags = re.findall(pattern, line)
    for tag in found_tags:
        tag_set.add(tag.translate(trantab).replace(" ", ""))

tag_list = list(tag_set)
tag_list.sort()
print(";".join((tag_list)))
