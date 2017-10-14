# https://www.codewars.com/kata/54df2067ecaa226eca000229

def f(n):
    if(isinstance(n, int) and n>0):
        return round((1+n)*n/2)
    else:
        return None
