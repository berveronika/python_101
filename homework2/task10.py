# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random
coins = int(input("Введите количество монет на столе: "))
heads = 0
tails = 0
for i in range(coins):
    this_coin = random.randint(0, 1)
    print(this_coin, end=" ")
    if this_coin == 0:
        heads += 1
    else:
        tails += 1
if heads < tails:
    print(f'\n{heads} монет надо перевернуть, чтобы все монетки были повернуты вверх одинаковой стороной')
else:
    print(f'\n{tails} монет надо перевернуть, чтобы все монетки были повернуты вверх одинаковой стороной')

