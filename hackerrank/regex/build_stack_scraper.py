# https://www.hackerrank.com/challenges/stack-exchange-scraper

import re

pattern = r'question-summary-(\w\w\w\w\w)"[\w\W]*?class="question-hyperlink">([\w\W]+?)</a>[\w\W]*?class=\"relativetime\">([\w\W]+?)</span>'
r'<h3><a href="/questions/\d+.+class="question-hyperlink">.+</a>[\d\D]*class="relativetime">\d\d hours ago'

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break
code = "\n".join(lines)

for match in re.finditer(pattern, code):
    print("{};{};{}".format(match.group(1), match.group(2), match.group(3)))
