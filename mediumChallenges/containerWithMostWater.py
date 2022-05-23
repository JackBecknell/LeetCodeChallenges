# You are given an integer list height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from distutils.command.build_scripts import first_line_re


def handle_calculations(height, length):
    volume = height * length
    return volume

def handle_volume_comparision(current_volume, check_volume):
    if current_volume >= check_volume:
        return current_volume
    else:
        return check_volume

def find_height_and_length(list):
    if list[0] >= list[-1]:
        height = list[-1]
    else:
        height = list[0]
    length = len(list)-1
    return [height, length]


def find_largest_container(int_list):
    original_length = len(int_list)
    height_and_length = find_height_and_length(int_list)
    volume = handle_calculations(height_and_length[0], height_and_length[1])
    for (index1, item) in enumerate(int_list):
        if len(int_list[index1:original_length]) < 2:
            continue
        check_list_one = int_list[index1: original_length]
        print(f'First for loop: {check_list_one}')
        check_h_l = find_height_and_length(check_list_one)
        check_v = handle_calculations(check_h_l[0], check_h_l[1])
        volume = handle_volume_comparision(volume, check_v)
        negative_index = original_length
        for (index2, item) in enumerate(check_list_one):
            if index2 == 0:
                negative_index -= 1
                continue
            else:
                check_list_two = int_list[index1:negative_index]
                print(f'Second for loop: {check_list_two}')
                check_h_l = find_height_and_length(check_list_two)
                check_v = handle_calculations(check_h_l[0], check_h_l[1])
                volume = handle_volume_comparision(volume, check_v)
                negative_index -= 1
        if len(int_list[0:index1]) >= 2:
            print('and we iterate')
    print(volume)
        # if index != 0:
        #     check_list_two = int_list[0:index]
        
find_largest_container([10,10,1,1,6,3])

# def find_largest_container(int_list):
#     first_index = int_list[0]
#     last_index = int_list[-1]
#     if first_index >= last_index:
#         height = last_index
#     else:
#         height = first_index
#     length = (len(int_list)-1)
#     volume = handle_calculations(height, length)
#     print(int_list[1:-1])





    # for indexes, if at any other index the height of current x space in between >= current volume than set variables to equal that
