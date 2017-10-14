# https://www.codewars.com/kata/550f22f4d758534c1100025a

def dirReduc(arr):
    opposites = {
        'NORTH' : 'SOUTH',
        'SOUTH' : 'NORTH',
        'EAST' : 'WEST',
        'WEST' : 'EAST',
        }
    i = 0
    while (i < len(arr)-1):
        if (arr[i+1] == opposites[arr[i]]):
            del arr[i]
            del arr[i]
            i = 0
        else:
            i += 1
    return arr
