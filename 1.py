# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 0,56 -> 11

# На семинаре сказали, что нужно считать сумму цифр полсе запятой

num = input('Введите вещественное число -> ')
divided_num = num.split('.')

res = 0

for item in divided_num[1]:
  res += int(item)


print(f'Сумма цифр дробной части = {res}')

# Еще сделал подсчет всех цифр в вещественном числе

num = input('Введите вещественное число -> ')
divided_num = num.split('.')

res = 0

for i in range(len(divided_num)):
  for item in divided_num[i]:
    res += int(item)

print(f'Сумма цифр = {res}')