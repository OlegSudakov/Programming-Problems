# https://www.hackerrank.com/challenges/dynamic-array

n, q = input().split(' ')
n, q = int(n), int(q)

seqList = []
for i in range(n):
    seqList.append([])

lastAnswer = 0
    
for i in range(q):
    t, x, y = input().split(' ')
    x, y = int(x), int(y)
    if t == "1":
        seqList[(x^lastAnswer) % n].append(y)
    elif t == "2":
        seq = seqList[(x^lastAnswer) % n]
        lastAnswer = seq[y % len(seq)]
        print(lastAnswer)
