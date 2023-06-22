# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = int(input('Введите трёхзначное число: '))
summa = 0
while number > 0:
    temp = number % 10
    summa = summa + temp
    number = number // 10
print(f'Сумма цифр числа равна: {summa}')