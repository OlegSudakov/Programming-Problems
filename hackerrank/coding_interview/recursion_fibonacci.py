# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers

memory = {}

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n not in memory:
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]
n = int(input())
print(fibonacci(n))
