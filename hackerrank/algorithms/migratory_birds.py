# https://www.hackerrank.com/challenges/migratory-birds

import sys

def migratoryBirds(n, ar):
    birds = {}
    for bird in ar:
        if bird in birds:
            birds[bird] += 1
        else:
            birds[bird] = 1
    max_count = max(birds.values())
    for ind in sorted(birds.keys()):
        if birds[ind] == max_count:
            return ind
        

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
