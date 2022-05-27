# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum (nums, target):
    for (index1, num1) in enumerate(nums):
        for (index2, num2) in enumerate(nums):
            if index2 == index1:
                continue
            elif num1 + num2 == target:
                return [index1, index2]
value = twoSum([5,2,3,9], 12)
print(value)

