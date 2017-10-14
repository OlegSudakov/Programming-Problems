# https://www.codewars.com/kata/546937989c0b6ab3c5000183

import string

def encryptor(key, message):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    res = ""
    for letter in message:
        if (letter in lowercase):
            index = (lowercase.index(letter)+key)%len(lowercase)
            if (index < 0): index+=len(lowercase)
            res += lowercase[index]
        elif (letter in uppercase):
            index = (uppercase.index(letter)+key)%len(uppercase)
            if (index < 0): index+=len(lowercase)
            res += uppercase[index]
        else:
            res += letter
    return res
