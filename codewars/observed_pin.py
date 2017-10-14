# https://www.codewars.com/kata/5263c6999e0f40dee200059d

near_digits = {'1': ['1','2','4'],
               '2': ['1','2','3','5'],
               '3': ['2','3','6'],
               '4': ['1','4','5','7'],
               '5': ['2','4','5','6','8'],
               '6': ['3','5','6','9'],
               '7': ['4','7','8'],
               '8': ['5','7','8','9','0'],
               '9': ['6','8','9'],
               '0': ['8','0']
               }

def get_pins(observed):
    result = []
    for new_digit in near_digits[observed[0]]:
        result.append(new_digit)
    for digit in observed[1:]:
        result = result*len(near_digits[digit])
        result.sort()
        i = 0
        while (i < len(result)):
            for new_digit in near_digits[digit]:
                result[i] += new_digit
                i+=1
    return result  
