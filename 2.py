# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
#     второй и предпоследний и т.д.

#     Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers_1 = [2, 3, 4, 5, 6]
numbers_2 = [2, 3, 5, 6]
numbers_3 = [2, 3, 5, 6, 7, 9, 10]
numbers_4 = [2, 3, 5, 7, 9, 10]

def mult_pair_numbers(numbers):
  res = []
  odd = 0
  
  if len(numbers) % 2 != 0:
    odd = 1;

  for i in range(len(numbers) // 2 + odd):
    r = numbers[i] * numbers[-1-i]
    res.append(r)
  return res

print(mult_pair_numbers(numbers_1))
print(mult_pair_numbers(numbers_2))
print(mult_pair_numbers(numbers_3))
print(mult_pair_numbers(numbers_4))