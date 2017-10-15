# https://www.hackerrank.com/challenges/maximum-element

stack = []

n = int(input())
for i in range(n):
    line = input()
    if line[0] == "1":
        op, x = line.split(" ")
        op, x = int(op), int(x)
        stack.append(x)
    if line[0] == "2":
        stack.pop()
    if line[0] == "3":
        print(max(stack))
