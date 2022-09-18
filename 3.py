# 3. Задайте последовательность чисел. Напишите программу, которая выведет список
#     неповторяющихся элементов исходной последовательности.
#     [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


def unique_list_items(list_numbers):
  unique_numbers = []
  for number in list_numbers:
    entry = 0
    for item in list_numbers:
      if item == number:
        entry += 1
        if entry == 2:
          break
    if entry < 2:
      unique_numbers.append(number)

  return unique_numbers

n = [0, 1, 1, 2, 3, 4, 5, 5, 6]

print(unique_list_items(n))