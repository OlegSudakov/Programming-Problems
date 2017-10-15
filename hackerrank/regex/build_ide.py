# https://www.hackerrank.com/challenges/programming-language-detection

import re

java_pat = r"(public|import\s+java|System.out.println)"
c_pat = r"#include<"
python_pat = r"(\s+def\s+[\w\d]+\(|print\s+[\d\w]+)"

lines = []
while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:
        break
code = "\n".join(lines)

if re.search(java_pat, code):
    print("Java")
elif re.search(c_pat, code):
    print("C")
elif re.search(python_pat, code):
    print("Python")
