# Задача 16: Требуется вычислить, сколько раз встречается некоторое 
# число X в массиве A[1..N]. Пользователь в первой строке вводит 
# натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Input N: '))
x = 4
list_ = []
count = 0
for i in range(1, n + 1):
    list_.append(i)
if x in list_:
    count += 1
else:
    count = 0
print(*list_)
print(x)
print(f'-> {count}')