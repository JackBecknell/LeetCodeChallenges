# Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring2(s):
    # working list hold s the current set of non-duplicate chars
    working_list = []
    # return value holds the longes yet iteration of non-duplicates
    return_value = 0
    index = 0
    while index < len(s):
        if s[index] in working_list:
            if len(working_list) > return_value:
                return_value = len(working_list)
            reversed_list = working_list[::-1]
            working_list = [s[index]]
            for i in reversed_list:
                if i != s[index]:
                    working_list.insert(0, i)
                else:
                    break
        else:
            working_list.append(s[index])
        index += 1
    return_value = max(return_value, len(working_list))
    return return_value

answer = lengthOfLongestSubstring2('aabaabgh')
print(answer)


# First attempt VVV

# def lengthOfLongestSubstring(s):
#     string_length = len(s)
#     index = 0
#     return_value = 0
#     while index < string_length:
#         compare_list = []
#         check_list = s[index:string_length]
#         for char in check_list:
#             if char in compare_list:
#                 if len(compare_list) > return_value:
#                     return_value = len(compare_list)
#                 compare_list = [char]
#                 continue
#             else:
#                 compare_list.append(char)
#         if len(compare_list) > return_value:
#             return_value = len(compare_list)
#         index += 1
#     return return_value

# value = lengthOfLongestSubstring2("dvdvcs")
# print(value)

# Logical walkthrough

# for the length of a string
# take char at incrementing index
# if that character is not in a comparing list
    # then add it
# if that character is in the comparing list
    # check length to see if it is the longest
        # if it is the longest than make that the return value
    # then delete everything at and behind that matching character