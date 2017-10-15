# https://www.hackerrank.com/challenges/ctci-balanced-brackets

def is_matched(expression):
    l = []
    for char in expression:
        if char in '({[':
            l.append(char)
        if char in '}])':
            if not l:
                return False
            if char == '}' and l[-1] != '{':
                return False
            if char == ')' and l[-1] != '(':
                return False
            if char == ']' and l[-1] != '[':
                return False
            l.pop()
    if not l:
        return True
    return False

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
