
"""Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13
Задание необходимо решать через рекурсию"""


# def fib(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     return fib(n - 2) + fib(n - 1)
#
#
# def fib_while(n):
#     if n == 1 or n == 2:
#         return 1
#     first = 1
#     second = 1
#     temp = first + second
#     count = 3
#     while count < n:
#         first = second
#         second = temp
#         temp = first + second
#         count += 1
#     return temp
#
#
# import time
#
# start = time.perf_counter()
# print(fib(30))
# end = time.perf_counter()
# duration = end - start
#
# start = time.perf_counter()
# print(fib_while(30))
# end = time.perf_counter()
# duration2 = end - start
#
# print(duration / duration2)


# import time
#
# print(time.perf_counter())
# print(time.perf_counter())

"""Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 4 10 20 1 2 
Output: 4 8 1 1 2
"""

# def change_marks(marks):
#     """Рекурсивная замена макисмальных оценок минимальными"""
#
#     max_mark = max(marks)
#     min_mark = min(marks)
#     marks[marks.index(max_mark)] = min_mark
#
#     if max_mark not in marks:
#         return marks
#     return change_marks(marks)
#
#
# print(change_marks([1, 2, 3, 1, 5, 1, 3, 4, 4, 5, 4, 5]))


# n = int(input())
# some_list = []
# for _ in range(n):
#     number = int(input())
#     some_list.append(number)
# maxx = some_list[0]
# minn = some_list[0]
# for el in some_list:
#     if el < minn:
#         minn = el
#     if el > maxx:
#         maxx = el
# for ind in range(0, n):
#     if some_list[ind] == maxx:
#         some_list[ind] = minn
#
# print(some_list)


"""Задача №35. Решение в группах
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes"""

# n = int(input())
#
#
# def a(x):
#     for div in range(2, int(n ** 0.5) + 1):
#         if n % div == 0:
#             return 'no'
#     return 'yes'
#
#
# print(a(n))


"""Задача №37. 
Дано натуральное число N и
последовательность из N элементов.
Требуется вывести эту последовательность в
обратном порядке.
Примечание. В программе запрещается
объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 2 -> 3 4
Output: 4 3"""


# 2 вариант решения задачи
# def change(n):
#     if n == 0:
#         return ''
#     num = int(input())
#     return change(n-1)+f' {num}'
#
# n = int(input('Введите количество элементов = '))
# print(change(n))