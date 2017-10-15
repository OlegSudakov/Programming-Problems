# https://www.hackerrank.com/challenges/balanced-brackets

closures = {"}":"{", "]":"[", ")":"("}

n = int(input())

for i in range(n):
    stack = []
    correct = True
    line = input()
    for char in line:
        if char in "{[(":
            stack.append(char)
        elif char in "}])":
            if stack:
                last_char = stack.pop()
                if last_char != closures[char]:
                    correct = False
                    break
            else:
                correct = False
    if len(stack) != 0:
        correct = False
    if correct:
        print("YES")
    else:
        print("NO")
