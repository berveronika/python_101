# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных
# чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def Weird_Sum(first, second = int): 
    if second == 0:
        return first
    else:
        return Weird_Sum(first + 1, second - 1)
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
print(f"Сумма чисел {number1} и {number2} равна {Weird_Sum(number1, number2)}")