# https://www.hackerrank.com/challenges/html-attributes

import re

tag_pattern = r"<(\w+)[^<]*>"
attr_pattern = r'(\w+)=["\']'

n = int(input())

tags = set()
atts = {}

for i in range(n):
    line = input()
    for match in re.finditer(tag_pattern, line):
        tagline = match.group(0)
        tag = match.group(1)
        tags.add(tag)
        for a_match in re.finditer(attr_pattern, tagline):
            attr = a_match.group(1)
            if tag in atts:
                atts[tag].add(attr)
            else:
                atts[tag] = set()
                atts[tag].add(attr)
tags = list(tags)
tags.sort()
for tag in tags:
    if tag in atts:
        attributes = list(atts[tag])
        attributes.sort()
        print("{}:{}".format(tag, ",".join(attributes)))
    else:
        print("{}:".format(tag))
