calls = 0


def count_calls():
    global calls
    calls += 1


count_calls()


def string_info(string_1):
    len_ = len(string_1)
    tup_ = (len_, string_1.upper(), string_1.lower())
    print(tup_)
    return string_1


count_calls()

string_info('Capybara')


def is_contains(string, list_to_search):
    for i in list_to_search:
        if string in i:
            print('True')
        else:
            print('Fals')
        return i


count_calls()

is_contains('ban', ['ban', 'BaNaN', 'urBAN'])
print(calls)
