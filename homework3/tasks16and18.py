# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
size = int(input("Введите количество чисел в списке: "))
find = int(input("Введите число, которое хотите найти в списке: "))
numbers = list()
count = 0
for i in range(size-1):
    numbers.append(random.randint(1, 10))
    print(numbers[i], end=" ")
    if numbers[i] == find:
        count += 1
if count > 0:
    print(f"\nЧисло {find} встречается {count} раз в списке.")
else:
    closest = 0
    for j in numbers:
        if abs(find - numbers[j]) < abs(closest - find):
            closest = numbers[j]
    print(f"\nВ списке нет числа {find}, ближайшее к нему число - {closest}")
