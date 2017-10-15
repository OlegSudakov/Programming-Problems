# https://www.hackerrank.com/challenges/find-point

n = int(input())

for i in range(n):
    line = input().strip().split(" ")
    line = [int(num) for num in line]
    p1, p2, q1, q2 = line
    r1 = q1 + (q1 - p1)
    r2 = q2 + (q2 - p2)
    print("{} {}".format(r1, r2))
