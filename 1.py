# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

#     Пример:

# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

numbers = [2, 3, 5, 9, 3]

def sum_num_list(numbers):
  sum = 0
  for i in range(1, len(numbers)):
    if i % 2 != 0:
      sum += numbers[i]
  return sum

print(sum_num_list(numbers))