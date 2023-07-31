# list
# some_list = []
# print(type(some_list))

# some_list = [1, 4.34, 'hello', True, [1, 2, 3]]
# print(some_list)
#
# print(some_list[-1])
#
# print(some_list[::-1])

# Вводится кол-во чисел, затем сами числа. Добавьте в список только четные числа

# count = int(input('Введите кол-во чисел: '))
# some_list = []
# for _ in range(count):
#     number = int(input())
#     if number % 2 == 0:
#         some_list.append(number)
# print(some_list)

# some_list = [1, 2, True, 'Hello']
#
# for el in some_list:
#     print(el)
#
# for ind in range(0, len(some_list)):
#     print(some_list[ind])


# tuple - кортеж
# some_tuple = tuple(some_list)
# print(some_tuple)
#
# some_tuple = (1, 2, 3, 4)

"""1.Создайте список из случайных чисел.
Найдите индекс его последнего локального максимума
(локальный максимум — это элемент, который больше любого из своих соседей)."""

# import random
#
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# [1, 10, 2, 0, 7, 4, 8, 5] -> 6
# РЕШЕНИЕ НИЖЕ...

# local_max = None
# for ind in range(1, len(some_list) - 1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
# print(local_max)

# local_max = None
# for ind in range(len(some_list) - 2, 0, -1):
#     if some_list[ind - 1] < some_list[ind] > some_list[ind + 1]:
#         local_max = ind
#         break
# print(local_max)


# 2.Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
#
# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)

# [9, 1, 2, 6, 10, 6, 7, 4, 10, 2]
# max_count = 0
# for el in some_list:
#     amount = 0
#     for i in some_list:
#         if el == i:
#             amount += 1
#     if amount > max_count:
#         max_count = amount
# print(max_count)

# max_count = 0
# for el in some_list:
#     amount = some_list.count(el)
#     if amount > max_count:
#         max_count = amount
# print(max_count)


# 17. Дан список чисел. Определите, сколько в нем встречается различных чисел.
"""
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""
# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)
#
# new_list = []
# for el in some_list:
#     if el not in new_list:
#         new_list.append(el)
# print(len(new_list))


"""Задача №19. Общее обсуждение
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 2
Output: [4, 5, 1, 2, 3]
"""

# import random
#
# count = int(input('Введите кол-во элементов: '))
# some_list = []
# for _ in range(count):
#     number = random.randint(0, 10)
#     some_list.append(number)
# print(some_list)
#
# k = int(input('Введите число для сдвига: '))
#
# nums = some_list[-k:] + some_list[:-k]
# print(nums)

"""Дан список, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов списка, больших предыдущего (элемента
с предыдущим номером)

Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)"""

# some_list = [0, -1, 5, 2, 3]
# amount = 0
# for ind in range(1, len(some_list)):
#     if some_list[ind - 1] < some_list[ind]:
#         amount += 1
# print(amount)


