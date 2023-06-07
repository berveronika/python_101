# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def Exponentiation(base, power):
    if power == 1:
        return base
    else:
        return base * Exponentiation(base, power - 1)

number = int(input("Введите число для возведения в степень: "))
exponent = int(input("Введите степень: "))
print(f'Число {number} в степени {exponent}: {Exponentiation(number, exponent)}')