first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first != second != third and first != third != second:
    print('Все числа разные "0"')
elif first == second == third:
    print('Все 3 числа равны')
elif (first == second or
      second == third or
      first == third):
    print('2 числа равны')

