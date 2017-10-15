# https://www.hackerrank.com/challenges/maximum-perimeter-triangle

n = int(input().strip())
arr = list(map(int, input().strip().split(" ")))
arr.sort(reverse = True)

pos = min(3, len(arr)-1)

a, b, c = arr[:3]
flag = False
while not flag:
    a, b, c = sorted([a, b, c], reverse = True)
    try:
        if a >= b + c:
            a = arr[pos]
            pos += 1
        else:
            if b >= a + c:
                b = arr[pos]
                pos += 1
            else:
                if c >= a + b:
                    c = arr[pos]
                    pos += 1
                else:
                    flag = True            
    except:
        print(-1)
        break
a, b, c = sorted([a, b, c])
if flag:
    print("{} {} {}".format(a, b, c))
