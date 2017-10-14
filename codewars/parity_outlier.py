# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(integers):
    for i in range(1, len(integers)-1):
        if (integers[i-1]%2 != integers[i]%2 and integers[i-1]%2 != integers[i+1]%2): return integers[i-1]
        if (integers[i]%2 != integers[i-1]%2 and integers[i]%2 != integers[i+1]%2): return integers[i]
        if (integers[i+1]%2 != integers[i]%2 and integers[i+1]%2 != integers[i-1]%2): return integers[i+1]
