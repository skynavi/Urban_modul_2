calls = 0


def count_calls():
    global calls
    calls += 1


count_calls()


def string_info(string_1):
    len_ = len(string_1)
    tup_ = (len_, string_1.upper(), string_1.lower())
    return tup_


count_calls()


def is_contains(string, list_to_search):
    for i in list_to_search:
        if string in i:
            return True
        else:
            return False


count_calls()

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('ban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
