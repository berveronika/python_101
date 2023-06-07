# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

size = int(input('Введите рамер списка чисел: '))
list1 = [random.randint(0, 100) for _ in range(size)]
print(list1)
us_min = int(input('Введите минимум для поиска: '))
us_max = int(input('Введите максимум для поиска: '))
indexes = []
for i in range(size):
    if us_min <= list1[i] <= us_max:
        indexes.append(i)
print(f'Индексы элементов, принадлежащих заданному диапазону: {indexes}')