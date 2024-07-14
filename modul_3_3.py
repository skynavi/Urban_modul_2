def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(2, 'edee', c=False)
print_params(b=25)
print_params(c=[1, 2, 3])  # функции работают, заменяя те, что назначены по умолчанию
values_list = ['srt', True, 232]  # создали value_list
print(values_list)
values_dict = {'a': True, 'b': 237, 'c': True}  # создали словарь values_dict
print(values_dict)
print_params(*values_list)  # передали список в функцию value_list
print_params(**values_dict)  # передали словарь в функцию value_list
values_list_2 = ('bober', True)
print(values_list_2)
print_params(*values_list_2, 42)  # проверил, работает добавил в с=42
