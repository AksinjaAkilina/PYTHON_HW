# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input('Введите число: '))
ind = 0
while 2 ** ind <= number:
    print(2 ** ind)
    ind += 1