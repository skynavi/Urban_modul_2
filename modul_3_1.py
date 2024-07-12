calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

count_calls()



def string_info():
    string_1 = input('введите строку: ')
    len_ = len(string_1)
    tuple = (len_, string_1.upper(), string_1)
    print(tuple)
    return string_1
    count_calls() +1


string_info()

while True: #  я не понял как сделать циклическое выполнение, поэтому так...
    a = input('поиск: ')
    b = ['ban', 'BaNaN', 'urBAN']
    def is_contains(c, e):
        if c in e:
            print('True')

        if c not in e:
            print('Fals')
        count_calls() + 1


    is_contains(a, b)
    print(calls)
