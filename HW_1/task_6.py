# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number = int(input('Введите шестизначное число: '))
if 99999 < number < 1000000:
    summa1 = 0
    num1 = int(number / 1000)
    while num1 > 0:
        temp1 = num1 % 10
        summa1 = summa1 + temp1
        num1 = num1 // 10
    print(summa1)
    summa2 = 0
    num2 = number % 1000
    while num2 > 0:
        temp2 = num2 % 10
        summa2 = summa2 + temp2
        num2 = num2 // 10        
    print(summa2)
    if summa1 == summa2:
        print('Вам попался счастливый билет!')
    else:
        print('Увы, билет не счастливый')
else:
    print('Это не шестизначное число')