# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать
# без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго
# множества. Затем пользователь вводит сами элементы множеств.

import random
fisrt_size = int(input('Введите количество элементов в первом наборе: '))
second_size = int(input('Введите количество элементов во втором наборе: '))
MIN_NUM = 0
MAX_NUM = 10
first_numbers = list()
for i in range(fisrt_size):
    first_numbers.append(random.randint(MIN_NUM, MAX_NUM))
print(first_numbers)
second_numbers = list()
for j in range(second_size):
    second_numbers.append(random.randint(MIN_NUM, MAX_NUM))
print(second_numbers)
result = list(set(first_numbers).intersection(set(second_numbers)))
result.sort()
print(result)