# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
#     "20" -> [2, 2, 5]


def prime_multipliers(number):
  list_multipliers = []
  multiplier = 2
  while multiplier <= number:
    if number % multiplier == 0:
      number /= multiplier
      list_multipliers.append(multiplier)
      multiplier = 2
    else:
      multiplier += 1
  return list_multipliers

print(prime_multipliers(20))
print(prime_multipliers(123))
print(prime_multipliers(568))