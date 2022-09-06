# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#     Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Так как в задаче нужно не просто вычислить факториал, а еще и вывести
# произведения, то сделал данным способом


number = int(input('Введите число -> '))

def factorial(n):
  if n < 0:
    return 'Параметр должен быть больше 0'

  expressions = ''
  if (n == 1) or (n == 0):
    expressions = '1'
    print(expressions)
    return 1
  call_func = factorial(n - 1)
  res = n * call_func
  expressions = f'{call_func} * {n} = {res}'
  print(expressions)
  return res

print(f'\nФакториал {number} = {factorial(number)}')

# Только вычисление факториала

def factorial(n):
  if n < 0:
    return 'Параметр должен быть больше 0'
  if (n == 1) or (n == 0):
     return 1
  return n * factorial(n - 1)

print(factorial(5))