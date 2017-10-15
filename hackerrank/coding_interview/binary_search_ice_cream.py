# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

t = int(input().strip())
for a0 in range(t):
    m = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    dict = {}
    for i in range(len(a)):
        dict[a[i]] = i
    for j in range(len(a)):
        if (m-a[j]) in dict:
            i = dict[m-a[j]]
            if i < j:
                print("{} {}".format(i+1,j+1))
                break
            elif i > j:
                print("{} {}".format(j+1,i+1))
                break
            else:
                continue
