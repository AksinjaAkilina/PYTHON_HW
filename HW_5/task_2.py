# 2.Создайте список из случайных чисел. Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

import random
count = int(input('Введите количество чисел: '))
some_list = [random.randint(1,10) for _ in range(count)]
print(some_list)

local_max = 0
local_i = 0
for i in range(1, 5):
    if some_list[i] > some_list[i-1]:
        if some_list[i] > some_list[i+1]:
            local_max = some_list[i]
            local_i = i
print(local_max, local_i)