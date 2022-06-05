# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

#!!! Unfinished, plan to come back to this. !!!

def permute(nums):
    result = []
    if (len(nums)==1):
        return [nums[:]]

    for i in range(len(nums)):
        num = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(num)
        result.extend(perms)
        nums.append(num)
    return nums

value = permute([1,2,3])
print(value)

# def findAllPermutations(list_int):
#     list_int_copy = list_int.copy()
#     if len(list_int) == 1:
#         return [list_int]
#     else:
#         return_value = []
#         for (i, value) in enumerate(list_int):
#             num = list_int_copy.pop(i)
#             append_this = findAllPermutations(list_int_copy)
#             if append_this[0][0]:  
#                 for (i, value) in enumerate(append_this):
#                     append_this[0][i].append(num)
#             for (i, value) in enumerate(append_this):
#                 append_this[i].append(num)
#             return_value.append(append_this)
#             for (i2, value2) in enumerate(return_value):
#                 print(f'this is i2: {i2}')
#                 print(f'this is value2: {value2}')
#             return return_value

# value = findAllPermutations([1,2,3])
# print(value)            