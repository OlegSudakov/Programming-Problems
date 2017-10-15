# https://www.hackerrank.com/challenges/crush

n, m = input().split(' ')
n, m = int(n), int(m)

arr = [0]*n

for i in range(m):
    a, b, k = input().split(' ')
    a, b, k = int(a), int(b), int(k)
    arr[a-1] += k
    if b < n:
        arr[b] -= k
    
x = 0
max_x = 0
for elem in arr:
    x += elem
    if x > max_x:
        max_x = x
print(max_x)
        
