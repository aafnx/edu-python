# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def is_weekend():
  day = int(input('Введите номер дня -> '))
  if day == 6 or day == 7:
    print('Выходной день')
  elif 0 < day < 6:
    print('Рабочий день')
  else:
    print('Неверноe значение, введите номер дня недели')

is_weekend()

# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def is_truth_statements(x, y, z):
  result = (not (x or y or z)) == (not x and not y and not z)
  print(f'утверждение {x}, {y}, {z} = {result}')

is_truth_statements(0,0,0)
is_truth_statements(0,0,1)
is_truth_statements(0,1,0)
is_truth_statements(0,1,1)
is_truth_statements(1,0,0)
is_truth_statements(1,0,1)
is_truth_statements(1,1,0)
is_truth_statements(1,1,1)



# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def show_quarter_number_by_coordinates():
  point_x = int(input('Введите координату X -> '))
  point_y = int(input('Введите координату Y -> '))
  quarter = 0

  if point_x > 0 and point_y > 0:
    quarter = 1
  elif point_x < 0 and point_y > 0:
    quarter = 2
  elif point_x < 0 and point_y < 0:
    quarter = 3
  elif point_x > 0 and point_y < 0:
    quarter = 4
  else:
    print('Вы ввели неккоретное значение')
    return

  print(f'Точка ({point_x}, {point_y}) находится в плоскости {quarter}')

show_quarter_number_by_coordinates()

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

def get_range_points_on_ccordinate(quarter):
  point_x_from = 0
  point_x_to = 0
  point_y_from = 0
  point_y_to = 0

  if quarter == 1:
    point_x_to = float('inf')
    point_y_to = float('inf')
  elif quarter == 2:
    point_x_to = float('-inf')
    point_y_to = float('inf')
  elif quarter == 3:
    point_x_from = float('-inf')
    point_y_from = float('-inf')
  elif quarter == 4:
    point_x_to = float('inf')
    point_y_from = float('-inf')
  
  print(f'Точка в четверти {quarter} может иметь кординату X от {point_x_from} до {point_x_to}, кординату Y от {point_y_from} до {point_y_to}')

get_range_points_on_ccordinate(1)
get_range_points_on_ccordinate(2)
get_range_points_on_ccordinate(3)
get_range_points_on_ccordinate(4)


# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

def get_distance_between_two_points():
  point_A = []
  point_B = []


  for i in range(2):
    current_list = point_A
    point = 'A'
    if i == 1:
      current_list = point_B
      point = 'B'

    for i in range(2):
      coordinate = 'X'
      if i == 1:
        coordinate = 'Y'

      num = int(input(f'Точка {point}, координата {coordinate} -> '))
      current_list.append(num)

  side_A = point_B[0] - point_A[0]
  side_B = point_B[1] - point_A[1]

  result = math.sqrt(side_A**2 + side_B**2)
  result = round(result, 3)

  print(f'Расстояние между точками А({point_A[0]},{point_A[1]}) и B({point_B[0]},{point_B[1]}) = {result}')


get_distance_between_two_points()