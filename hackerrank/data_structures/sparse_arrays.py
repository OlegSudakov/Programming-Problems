# https://www.hackerrank.com/challenges/sparse-arrays

n = int(input())

strings = {}

for i in range(n):
    string = input()
    if string in strings:
        strings[string] += 1
    else:
        strings[string] = 1
    
q = int(input())

for i in range(q):
    query = input()
    if query in strings:
        print(strings[query])
    else:
        print("0")
