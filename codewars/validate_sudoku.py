# https://www.codewars.com/kata/540afbe2dc9f615d5e000425

import math

class Sudoku(object):
    #your code here
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.height = len(sudoku)
        self.width = len(sudoku[0])
        
    def check_dimensions(self):
        widths = [len(row) for row in self.sudoku]
        for width in widths:
            if (width != self.width):
                return False
        if (self.height != self.width): return False
        if (math.sqrt(self.height) % 1 != 0 or math.sqrt(self.width) % 1 != 0):
            return False
        return True

    def check_values(self):
        for row in self.sudoku:
            for number in row:
                if (not (type(number) is int)):
                    return False
                if (number < 1 or number > self.height):
                    return False
        return True

    def check_rows(self):
        for row in self.sudoku:
            if (len(set(row)) != len(row)):
                return False
        return True

    def check_columns(self):
        for i in range(self.width):
            column = [self.sudoku[j][i] for j in range(self.height)]
            if (len(set(column)) != len(column)):
                return False
        return True

    def check_squares(self):
        for i in range(0, self.height-1, round(math.sqrt(self.height))):
            for j in range(0, self.width-1, round(math.sqrt(self.width))):
                square_elems = []
                for k in range(round(math.sqrt(self.height))):
                    for l in range (round(math.sqrt(self.width))):
                        square_elems.append(self.sudoku[j+l][i+k])
                if (len(set(square_elems)) != len(square_elems)):
                    return False
        return True
        
    def is_valid(self):
        return (self.check_dimensions() and self.check_values() and self.check_rows() and self.check_columns() and self.check_squares())
