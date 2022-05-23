# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

from distutils.command.build_scripts import first_line_re


def handle_calculations(height, length):
    volume = height * length
    return volume

def handle_comparision(current_volume, check_volume):
    if current_volume >= check_volume:
        return current_volume
    else:
        return check_volume


def find_largest_container(int_array):
    first_index = int_array[0]
    last_index = int_array[-1]
    if first_index >= last_index:
        height = last_index
    else:
        height = first_index
    length = (len(int_array)-1)
    volume = handle_calculations(height, length)
    print(int_array[1:-1])


find_largest_container([3,4,1,1,4,3])


    # for indexes, if at any other index the height of current x space in between >= current volume than set variables to equal that
