# https://www.hackerrank.com/challenges/tree-huffman-decoding

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    result = ""
    current = root
    for ch in s:
        if ch == "0":
            current = current.left
        if ch == "1":
            current = current.right
        if current.left is None and current.right is None:
            result += current.data
            current = root
    print(result)
