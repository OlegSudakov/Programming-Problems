# https://www.hackerrank.com/challenges/ctci-contacts

class ContactBook:
    def __init__(self):
        self.book = {}

    def add(self, contact):
        cur_dict = self.book
        for letter in contact:
            if letter in cur_dict:
                cur_dict[letter][1] += 1
                cur_dict = cur_dict[letter][0]
            else:
                cur_dict[letter] = [{}, 1]
                cur_dict = cur_dict[letter][0]

    def lookup(self, contact):
        cur_dict = self.book
        last_n = 0
        for letter in contact:
            if letter in cur_dict:
                last_n = cur_dict[letter][1]
                cur_dict = cur_dict[letter][0]
            else:
                return 0
        return last_n

n = int(input().strip())
cb = ContactBook()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        cb.add(contact)
    elif op == 'find':
        print(cb.lookup(contact))
