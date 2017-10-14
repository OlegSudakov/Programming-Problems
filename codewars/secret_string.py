# https://www.codewars.com/kata/53f40dff5f9d31b813000774

def recoverSecret(triplets):
    'triplets is a list of triplets from the secrent string. Return the string.'
    string = []
    for triplet in triplets:
        for letter in triplet:
            if (not letter in string):
                string.append(letter)
    flag = True
    while (flag):
        flag = False
        for triplet in triplets:
            if (string.index(triplet[0])>string.index(triplet[1])):
                a = string.index(triplet[0])
                b = string.index(triplet[1])
                string[a], string[b] = string[b], string[a]
                flag = True
            if (string.index(triplet[1]) > string.index(triplet[2])):
                a = string.index(triplet[1])
                b = string.index(triplet[2])
                string[a], string[b] = string[b], string[a]
                flag = True
    return "".join(string)
