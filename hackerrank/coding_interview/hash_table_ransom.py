# https://www.hackerrank.com/challenges/ctci-ransom-note

def ransom_note(magazine, ransom):
    words = {}
    for word in magazine:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for word in ransom:
        if word not in words:
            return False
        else:
            if words[word] == 0:
                return False
            words[word] -= 1  
    return True
    
m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
