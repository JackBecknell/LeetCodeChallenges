# FINISHED

# This recursive function will call itself as many times as it takes until the integer being passed through it has finally reached zero
# and the return array is complete.
def int_to_roman_list(integer, recursive_roman_list=False):
    if recursive_roman_list:
        return_value = recursive_roman_list
    else:
        return_value = []
    if integer >= 1000:
        return_value.extend(['M'])
        integer -= 1000
    elif integer >= 900:
        return_value.extend(['C','M'])
        integer -= 900
    elif integer >= 500:
        return_value.extend(['D'])
        integer -= 500
    elif integer >= 400:
        return_value.extend(['C','D'])
        integer -= 400
    elif integer >= 100:
        return_value.extend(['C'])
        integer -= 100
    elif integer >= 90:
        return_value.extend(['X','C'])
        integer -= 90
    elif integer >= 50:
        return_value.extend(['L'])
        integer -= 50
    elif integer >= 40:
        return_value.extend(['X','L'])
        integer -= 40
    elif integer >= 10:
        return_value.extend(['X'])
        integer -= 10
    elif integer >= 9:
        return_value.extend(['I','X'])
        integer -= 9
    elif integer >= 5:
        return_value.extend(['V'])
        integer -= 5
    elif integer >= 4:
        return_value.extend(['I', 'V'])
        integer -= 4
    elif integer >= 1:
        return_value.extend(['I'])
        integer -= 1
    if integer != 0:
        return_value = int_to_roman_list(integer, return_value)
    return return_value

def handle_int_to_roman_str(int):
    list_of_roman_chars = int_to_roman_list(int)
    return_value = ""
    for char in list_of_roman_chars:
        return_value += char
    return return_value

value = handle_int_to_roman_str(3424)
print(value)