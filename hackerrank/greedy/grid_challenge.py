# https://www.hackerrank.com/challenges/grid-challenge

t = int(input().strip())
for i in range(t):
    n = int(input().strip())
    flag = True
    lines = []
    l = list(input().strip())
    l.sort()
    lines.append(l)
    for i in range(n-1):
        l = list(input().strip())
        l.sort()
        lines.append(l)
        for t in range(n):
            if lines[-1][t] < lines[-2][t]:
                flag = False
    if flag:
        print("YES")
    else:
        print("NO")
