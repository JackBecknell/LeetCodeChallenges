from operator import index


lists = [[1,4,5,7],[1,3,4,8],[2,6,9]]
# Output: [1,1,2,3,4,4,5,6,7,8,9]

def handle_k_sort(listOfLists):
    return_value = []
    for list in listOfLists:
        for i in list:
            if len(return_value) == 0:
                return_value.append(i)
            else:
                num_added = False
                for return_value_index in range(len(return_value)):
                    if i <= return_value[return_value_index]:
                        return_value.insert(return_value_index, i)
                        num_added = True
                        break
                if num_added == False:
                    return_value.append(i)
    return return_value

value = handle_k_sort(lists)
print(value)
