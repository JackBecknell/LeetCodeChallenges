
# ROMAN TO INTEGER

roman_nums = "LVIII"

def handle_calculations (total_value, num, is_addition):
    if is_addition:
        return total_value + num
    else:
        return total_value - num

def convert_int_to_roman(arg_roman_nums):
    roman_nums = arg_roman_nums.upper()
    list_roman_nums = list(roman_nums)
    list_roman_nums.reverse()
    index = 0
    for i in list_roman_nums:
        if (i == "M"):
            num = 1000
            is_addition = True
        elif(i == "D"):
            num = 500
            is_addition = True
        elif(i == "C"):
            num = 100
            if(len(list_roman_nums) == 1 or index == 0):
                is_addition = True
            elif (list_roman_nums[index-1] == "D" or list_roman_nums[index-1] == "M"):
                is_addition = False
            else:
                is_addition = True
        elif(i == "L"):
            num = 50
            is_addition = True
        elif(i == "X"):
            num = 10
            if(len(list_roman_nums) == 1 or index == 0):
                is_addition = True
            elif (list_roman_nums[index-1] == "L" or list_roman_nums[index-1] == "C"):
                is_addition = False
            else:
                is_addition = True
        elif(i == "V"):
            num = 5
            is_addition = True
        elif(i == "I"):
            num = 1
            if(len(list_roman_nums) == 1 or index == 0):
                is_addition = True
            elif (list_roman_nums[index-1] == "V" or list_roman_nums[index-1] == "X"):
                is_addition = False
            else:
                is_addition =  True
        return_value = handle_calculations(return_value, num, is_addition)
        index = index+1

roman_nums_to_int = convert_int_to_roman("LVIII")
print(roman_nums_to_int)
