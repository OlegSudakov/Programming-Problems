def array_left_rotation(a, n, k):
    k = k % n
    a = list(a)
    a = a[k:] + a[:k]
    return a
    

n, k = map(int, input().strip().split(' '))
a = map(int, input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
