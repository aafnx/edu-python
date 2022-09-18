# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#     (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     Пример:
#         k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def get_polynomial(degree):
  polynomial = ''
  for _ in range(degree + 1):
    n = random.randint(0, 100)
    if n == 0:
      degree -= 1
      continue
    if degree == 0:
      polynomial += f'{n} = 0'
    elif degree == 1:
      polynomial += f'{n}x + '
    else:
      polynomial += f'{n}x^{degree} + '
    degree -= 1
    
  if 'x' not in polynomial:
    polynomial = 'Все коэфиценты были равны 0'

  if polynomial[-1] != '0':
    polynomial = polynomial[:-3]
    polynomial += ' = 0'

  return polynomial

print(get_polynomial(2))
print(get_polynomial(4))