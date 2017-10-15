# https://www.hackerrank.com/challenges/ctci-bubble-sort

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

swaps = 0
for j in range(n-1):
    for i in range(n-1):
        if a[i] > a[i+1]:
            swaps += 1
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp

print("Array is sorted in {} swaps.".format(swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1])) 
