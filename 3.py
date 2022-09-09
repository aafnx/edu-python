# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

#     Пример:

# - [1.1, 1.2, 3.1, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 4.0105]

def get_fractional_part(str_n):
  str_n = str(str_n)
  n = str_n.split('.')
  n = n[1]
  if len(n) > 1:
    len_n = len(n)
    n = float(n) / 10
    n /= 10 ** (len_n - 1)
  else:
    n = float(n) / 10
  return n

def get_difference_max_min(numbers):
  numb = get_fractional_part(numbers[0])
  max = numb
  min = numb

  for item in numbers[1:]:
    n = get_fractional_part(item)
    if n > max:
      max = n
    if n < min:
      min = n
  diff = max - min
  return diff

print(get_difference_max_min(numbers))