# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

n = int(input('Введите число N '))
i = 1
while i < n:
    print(i)
    i = i * 2
