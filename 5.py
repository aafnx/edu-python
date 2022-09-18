# 5. Даны два файла, в каждом из которых находится запись многочлена.
#     Задача - сформировать файл, содержащий сумму многочленов.


def get_data_from_file(path):
  data = open(path, 'r')
  res = data.read()
  data.close
  return res

def get_monomials(polynomial):
  res = polynomial.split(' + ')
  res[-1] = res[-1][:-4]
  return res

def get_nums_from_monomial(monomial):
  res = []
  for item in monomial:
    if len(item) == 1:
      res.append(int(item))
      continue
    num = ''
    for element in item:
      if element.isdigit():
        num += element
      else:
        break
    num = int(num)
    res.append(int(num))
      
  return res

def get_sum_polynomial(polynomial_1, polynomial_2):
  res = ''
  equation_1 = get_monomials(polynomial_1)
  equation_1 = get_nums_from_monomial(equation_1)
  equation_2 = get_monomials(polynomial_2)
  equation_2 = get_nums_from_monomial(equation_2)

  rng = 0
  length_difference = len(equation_1) - len(equation_2)
  length_difference = abs(length_difference)

  if length_difference > 0:
    if len(equation_1) > len(equation_2):
      rng = len(equation_1)
      for i in range(length_difference):
        equation_2.insert(i, 0)
    else:
      rng = len(equation_2)
      for i in range(length_difference):
        equation_1.insert(i, 0)

  sums = []

  for i in range(rng):
    n = equation_1[i] + equation_2[i]
    sums.append(n)

  degree_num = len(sums) - 1
  for item in sums:
    if degree_num == 0:
      res += f'{item} = 0'
    elif degree_num == 1:
      res += f'{item}x + '
    else:
      res += f'{item}x^{degree_num} + '
    degree_num -= 1
  return res

equation_1 = get_data_from_file('5-1.txt')
equation_2 = get_data_from_file('5-2.txt')

result = get_sum_polynomial(equation_1, equation_2)

file = open('5-res.txt', 'w')
file.write(result)
file.close()