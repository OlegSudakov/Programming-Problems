# https://www.codewars.com/kata/54b679eaac3d54e6ca0008c9

def get_double(n):
    return 2*n

def compose(f, g):
    return lambda x: f(g(x))

def create_iterator(func, n):
    if (n == 1):
        return func
    res = compose(func, func)
    for i in range(n-2):
        res = compose(res, func)
    return res
