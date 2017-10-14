# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

def DNA_strand(dna):
    res = ""
    DNA_dictionary = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'}
    for letter in dna:
        res = res + DNA_dictionary[letter]
    return res
