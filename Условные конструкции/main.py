'''
    Логические операторы
    > < == != >= <=

    Условный оператор
    if <условие>:
        <операторы>
        ...
    [elif <условие>:
        <операторы>
        ...]
    [else:
        <операторы>
        ...]
'''

num = int(input())
if num % 2 == 0:
    print('Число чётное')
else:
    print('Число нечётное')