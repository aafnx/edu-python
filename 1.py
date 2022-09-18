# 1. Вычислить число c заданной точностью d
#     Пример:
#         при $d = 0.001 (количество знаков после запятой,
#         которые нужно вывести у числа Пи,
#         π = 3.141 (на числе Пи проводить операции)

import math

def rounding_accuracy(float_n, accuracy):
  accuracy = str(accuracy)
  accuracy = accuracy.split('.')
  if len(accuracy) < 2:
    accuracy = (accuracy[0].split('-'))[1]
  else:
    accuracy = len(accuracy[1])
  accuracy = int(accuracy)
  float_n = round(float_n, accuracy)
  return float_n


print(rounding_accuracy(math.pi, 0.000001))
print(rounding_accuracy(math.pi, 0.001))