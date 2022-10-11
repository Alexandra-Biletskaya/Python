# Цикл for
sum = 0
for i in range(10):
    # Параметр end=' ' определяет чем оканчивается вывод print
    print(i, end=' ')
    # sum = sum + i
    sum += i
print(f'\nСумма чисел: {sum}')
