number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # создаем пустой список для primes
not_primes = []  # создаем пустой список для no_primes
for i in range(len(number) + 1):  # цикл длинной в количество элементов в списке
    is_prime = True  # создаем переменную внутри цикла и присваем ей True
    for j in range(2, int(i ** 0.5) + 1):  # описываем условие
        if i % j == 0:  # перебор всех чисел по условию
            is_prime = False
            break
    if i == 0:  # убиваем 0
        continue
    elif i == 1:  # убиваем 1
        continue
    elif is_prime:  # простые в прайм
        primes.append(i)
    elif not is_prime:
        not_primes.append(i)  # оставшиеся в не прайм
print('primes: ', primes)  # выводим решение
print('not_primes: ', not_primes)   # выводим решение
