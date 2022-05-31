# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number 
# could represent. Return the answer in any order.
# A mapping of digit to letters (just like on the telephone buttons). Note that 1 does not map 
# to any letters.

# CONSTRAINTS:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].


phone_number_to_letter_dict = {
  "0":[''],
  "1":[''],
  "2":["a","b","c"],
  "3":["d","e","f"],
  "4":["g","h","i"],
  "5":["j","k","l"],
  "6":["m","n","o"],
  "7":["p","q","r","s"],
  "8":["t","u","v"],
  "9":["w","x","y","z"]
  }

def letterCombinations (integer, dict):
    return_value = []
    nums_list = [str(x) for x in str(integer)]
    if '1' or '0' in nums_list:
        if nums_list.__contains__('0'):
            nums_list.remove('0')
        if nums_list.__contains__('1'):
            nums_list.remove('1')
    elif len(nums_list > 4):
        return('Sorry, this function was intended to recieve 4 digit integers.')
    correlated_letters_list = []
    for i in range(len(nums_list)):
        correlated_letters_list.append(dict[nums_list[i]])
    for i in correlated_letters_list[0]:
        if len(correlated_letters_list) == 1:
            return_value.append(i)
        else:
            for i2 in correlated_letters_list[1]:
                if len(correlated_letters_list) == 2:
                    return_value.append(i+i2)
                else:
                    for i3 in correlated_letters_list[2]:
                        if len(correlated_letters_list) == 3:
                            return_value.append(i+i2+i3)
                        else:
                            for i4 in correlated_letters_list[3]:
                                if len(correlated_letters_list) == 4:
                                    return_value.append(i+i2+i3+i4)
    return return_value
        

    

answer = letterCombinations(None,phone_number_to_letter_dict)
print(answer)

# for all dictionary values at zero index
    # add all values