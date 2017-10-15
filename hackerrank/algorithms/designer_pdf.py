# https://www.hackerrank.com/challenges/designer-pdf-viewer

import sys

h = list(map(int, input().strip().split(' ')))
word = input().strip()

max_h = -1
for char in word:
    if h[ord(char) - ord('a')] > max_h:
        max_h = h[ord(char) - ord('a')]
print(len(word)*max_h)


