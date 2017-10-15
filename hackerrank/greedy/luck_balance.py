# https://www.hackerrank.com/challenges/luck-balance

line = input().strip().split()
n = int(line[0])
k = int(line[1])
important = []
luck_balance = 0
for i in range(n):
    line = input().strip().split()
    if int(line[1]) == 0:
        luck_balance += int(line[0])
    else:
        important.append(int(line[0]))
important.sort(reverse = True)
for b in important:
    if (k > 0):
        luck_balance += b
        k -= 1
    else:
        luck_balance -= b
print(luck_balance)
