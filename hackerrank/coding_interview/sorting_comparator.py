# https://www.hackerrank.com/challenges/ctci-comparator-sorting

from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def comparator(a, b):
        if a.score < b.score:
            return 1
        elif a.score > b.score:
            return -1
        else:
            for i in range(min(len(a.name), len(b.name))):
                if ord(a.name[i]) < ord(b.name[i]):
                    return -1
                elif ord(a.name[i]) > ord(b.name[i]):
                    return 1
            if len(a.name) == len(b.name):
                return 0
            elif len(a.name) < len(b.name):
                return -1
            else:
                return 1
