# 4.Создайте список из случайных чисел. Найдите второй максимум.
# a = [1, 2, 3] # Первый максимум == 3, второй == 2.

import random
count = int(input('Введите количество чисел: '))
some_list = [random.randint(1,10) for _ in range(count)]
print(some_list)
max_el = max(some_list)
print(f'Первый максимум: {max_el}')
some_list.remove(max_el)
print(f'Второй максимум: {max(some_list)}')