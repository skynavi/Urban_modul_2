def get_multiplied_digits(number):
    number = str(number)
    str_number = str(number)
    first = int(str_number[0])
    if str_number == '0':
        str_number = str_number[:len(str_number) - 1]
    elif len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
