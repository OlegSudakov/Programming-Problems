# https://www.hackerrank.com/challenges/ctci-making-anagrams

def number_needed(a, b):
    aLetters = {}
    bLetters = {}
    for char in a:
        if char in aLetters:
            aLetters[char] += 1
        else:
            aLetters[char] = 1
    for char in b:
        if char in bLetters:
            bLetters[char] += 1
        else:
            bLetters[char] = 1
    dif = 0
    for char in aLetters:
        if char in bLetters:
            dif += abs(aLetters[char] - bLetters[char])
        else:
            dif += aLetters[char]
    for char in bLetters:
        if char not in aLetters:
            dif += bLetters[char]
    return dif
            
a = input().strip()
b = input().strip()

print(number_needed(a, b))
