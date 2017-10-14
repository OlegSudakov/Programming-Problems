# https://www.codewars.com/kata/5274d9d3ebc3030802000165

def gcd(a, b):
    if (b == 0): return a
    else: return gcd(b, a % b)

def nbr_of_laps(x, y):
    g = gcd(x,y)
    lcm = x*y/g
    return [round(lcm/x), round(lcm/y)]
