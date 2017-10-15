# https://www.hackerrank.com/challenges/counting-valleys

n = int(input().strip())
seq = input().strip()

h = 0
valleys = 0
for step in seq:
    if step == "U":
        if h == -1:
            valleys += 1
        h += 1
    if step == "D":
        h -= 1
print(valleys)
