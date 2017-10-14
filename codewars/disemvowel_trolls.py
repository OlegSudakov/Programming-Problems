# https://www.codewars.com/kata/52fba66badcd10859f00097e

def disemvowel(string):
    return "".join([letter for letter in string if letter.lower() not in ['a', 'e', 'o', 'i', 'u']])
