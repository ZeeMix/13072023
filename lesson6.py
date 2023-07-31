"""Задача №39. Решение в группах
Даны два массива чисел. Требуется вывести те элементы
первого массива (в том порядке, в каком они идут в первом
массиве), которых нет во втором массиве. Пользователь вводит
число N - количество элементов в первом массиве, затем N
чисел - элементы массива. Затем число M - количество
элементов во втором массиве. Затем элементы второго массива
Ввод:
7
3 1 3 4 2 4 12
6
4 15 43 1 15 1

Вывод:
3 3 2 12
"""
import time
import random

# n = int(input('Введите количество элементов в первом списке: '))
# first_set = set()
# second_set = set()
# for _ in range(n):
#     number = random.randint(1, 1000)
#     first_set.add(number)
#
# m = int(input('Введите количество элементов во втором списке: '))
# for _ in range(m):
#     number = random.randint(1, 1000)
#     second_set.add(number)
#
# start = time.perf_counter()
# dif = first_set.difference(second_set)
# end = time.perf_counter()
# duration_set = end - start
#
# # print(dif)
#
# first_list = list(first_set)
# second_list = list(second_set)
#
# start = time.perf_counter()
# for el in first_list:
#     if el not in second_list:
#         pass
#         # print(el, end=' ')
# end = time.perf_counter()
# duration_list = end - start
# print(duration_list / duration_set)


# n = int(input('Введите количество элементов в списке: '))
# first_set = set()
# for _ in range(n):
#     number = random.randint(1, 10 ** 6)
#     first_set.add(number)
#
# first_list = list(first_set)
#
# start = time.perf_counter()
# print(100000 in first_set)
# end = time.perf_counter()
# duration_set = end - start
#
# start1 = time.perf_counter()
# print(100000 in first_list)
# end1 = time.perf_counter()
# duration_list = end1 - start1
#
# print(duration_list / duration_set)


"""Дан массив, состоящий из целых чисел. Напишите
программу, которая в данном массиве определит
количество элементов, у которых два соседних и, при
этом, оба соседних элемента меньше данного. Сначала
вводится число N — количество элементов в массиве
Далее записаны N чисел — элементы массива. Массив
состоит из целых чисел."""


"""Ввод:
5
1 2 3 4 5

Вывод:
0

Ввод:
5
1 5 1 5 1

Вывод:
2
"""

# count = 0
# count_in_list1 = int(input('Введите кол-во элементов списка: '))
# list1 = [int(input('Введите элемент')) for _ in range(count_in_list1)]
# for i in range(1, len(list1) - 1):
#     if list1[i - 1] < list1[i] > list1[i + 1]:
#         count += 1
# print(count)

'''Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 3
Вывод:
2
'''


# count_in_list1 = int(input('Введите кол-во элементов списка: '))
# list1 = [int(input('Введите элемент ')) for i in range(count_in_list1)]
# print(list1)
# count = 0
# for i in set(list1):
#     count += list1.count(i) // 2
# print(count)

# n = int(input('введите количесво символов в первом списке: '))
# list1 = []
# for _ in range (n):
#     list1.append(int(input('введите значение элемента первого списка: ')))
# a = set(list1)
# count_res = 0
# for i in a:
#     count = 0
#     for j in list1:
#         if i == j:
#             count += 1
#     count_res += count // 2
# print(count_res)