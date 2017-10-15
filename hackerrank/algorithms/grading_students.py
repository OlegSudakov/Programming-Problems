# https://www.hackerrank.com/challenges/grading

import sys

def solve(grades):
    result = []
    for grade in grades:
        if grade >= 38:
            if grade % 10 == 3 or grade % 10 == 4:
                grade = (grade // 10)*10 + 5
            elif grade % 10 == 8 or grade % 10 == 9:
                grade = (grade // 10 + 1)*10
        result.append(grade)
    return result

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
