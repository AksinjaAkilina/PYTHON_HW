# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input('Введите количество журавликов: '))
if number % 6 == 0:
    a = int(number / 6)
    b = a * 4
    print(f'Петя сделал - {a}, Катя - {b}, а Сережа - {a} журавликов')
else:
    print('Очень жаль... Вы не смогли разгадать эту задачку')