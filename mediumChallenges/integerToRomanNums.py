# unfinished

def int_to_roman(integer):
    return_value = []
    working_value = integer
    remainder = 0
    if working_value >= 1000:
        remainder = working_value%1000
        roman_m = int(working_value/1000)
        for i in range(roman_m):
            return_value.append("M")
        if remainder == 0:
            return return_value
        else: 
            working_value = remainder
    if working_value >= 500:
        remainder = working_value%500
        roman_d = int(working_value/500)
        for i in range(roman_d):
            return_value.append("D")
        if remainder == 0:
            return return_value
        else: 
            working_value = remainder


value = int_to_roman(3500)
print(value)