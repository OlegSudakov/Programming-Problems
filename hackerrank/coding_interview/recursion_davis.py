# https://www.hackerrank.com/challenges/ctci-recursive-staircase

memory = {}

def compute_steps(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        if n in memory:
            return memory[n]
        else:
            memory[n] = compute_steps(n-1)+compute_steps(n-2)+compute_steps(n-3)
            return memory[n]

s = int(input().strip())
for a0 in range(s):
    n = int(input().strip())
    steps = compute_steps(n)
    print(steps)

