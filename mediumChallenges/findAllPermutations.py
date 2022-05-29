list1 = [1,2,3]
list2 = list1.copy()

list2.append(4)
print(f'This is list one: {list1}')
print(f'This is list two: {list2}')


def findAllPermutations(list_int):
    list_int_copy = list_int.copy()
    if len(list_int) == 1:
        return [list_int]
    else:
        return_value = []
        for (i, value) in enumerate(list_int):
            num = list_int_copy.pop(i)
            append_this = findAllPermutations(list_int_copy)
            if append_this[0][0]:  
                for (i, value) in enumerate(append_this):
                    append_this[0][i].append(num)
            for (i, value) in enumerate(append_this):
                append_this[i].append(num)
            return_value.append(append_this)
            for (i2, value2) in enumerate(return_value):
                print(f'this is i2: {i2}')
                print(f'this is value2: {value2}')
            return return_value

value = findAllPermutations([1,2,3])
print(value)            