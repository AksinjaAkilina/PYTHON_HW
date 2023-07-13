# 3.Создайте список из случайных чисел. 
# Найдите максимальное количество его одинаковых элементов.

import random
count = int(input('Введите количество чисел: '))
some_list = [random.randint(1,10) for _ in range(count)]
print(some_list)

new_dict = {}
result = 0
for i in some_list:
    if i in new_dict:
        new_dict[i] += 1
    else:
        new_dict[i] = 1
max_el = max(new_dict.values())
print(max_el)   