# https://www.codewars.com/kata/54e6533c92449cc251001667

def unique_in_order(iterable):
    return [iterable[i] for i in range(len(iterable)) if (i==0 or iterable[i]!=iterable[i-1])]
