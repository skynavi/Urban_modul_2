num_ = int(input('введите число от 3 до 20: '))
for i in range(1, num_):
    for j in range(i, num_):
        if num_ % (i + j) == 0 and i != j:
            for x in range(1):
                print(i, j, end=' ')
