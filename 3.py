# 3. Создайте программу для игры в ""Крестики-нолики""(консольная версия или библиотека tkinter).

def create_field():
  field = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
  ]
  return field



def check_win_in_field_line(mark, field, i): # строка
  count = 0
  for j in range(len(field[i])):
    if mark in field[i][j]: 
      count += 1
      if count == 3:
        return True

def check_win_in_field_row(mark, field, i): # столбец
  count = 0
  for j in range(len(field[i])):
    if mark in field[j][i]:
      count += 1
      if count == 3:
        return True

def check_win_in_field_diagonal(mark, field, i): # диагональ
  count = 0
  for j in range(len(field[i])):
    if mark in field[j][j]:
      count += 1
      if count == 3:
        return True

def check_win_in_field_diagonal_reverse(mark, field): # обратная диагональ
  count = 0
  x = 0
  y = 2
  for _ in range(len(field)):
    if mark in field[x][y]:
      count += 1
      if count == 3:
        return True
    x += 1
    y -= 1

def check_empty_cells_on_field(field):
  for line in field:
    if '_' in line:
      return True
  return False 

def check_winner(mark, field):
  for i in range(len(field)):
    if check_win_in_field_line(mark, field, i):
      return True
    if check_win_in_field_row(mark, field, i):
      return True
    if check_win_in_field_diagonal(mark, field, i):
      return True
    if check_win_in_field_diagonal_reverse(mark, field):
      return True

  return False

def parsing_coordinates(coordinates):
  coordinates = coordinates.split()
  coordinates = list(map(int, coordinates))
  return coordinates

def turn(field, coordinates, player):
  coordinates = parsing_coordinates(coordinates)
  while check_mark_in_cell_field(field, coordinates):
    print(f'Ячейка занята!')
    coordinates = input(f'Ход {player}. Введите координаты (через пробел) -> ')
    coordinates = parsing_coordinates(coordinates)
  x = coordinates[0]
  y = coordinates[1]
  field[x][y] = player


def check_mark_in_cell_field(field, coordinates):
  x = coordinates[0]
  y = coordinates[1]
  if '_' not in field[x][y]:
    return True
  return False

def render_field(field):
  print(f'\n\n                  | {field[0][0]} | {field[0][1]} | {field[0][2]} |')
  print(f'                  | {field[1][0]} | {field[1][1]} | {field[1][2]} |')
  print(f'                  | {field[2][0]} | {field[2][1]} | {field[2][2]} |\n\n')


def game(field):
  is_turn_X = True
  player = 'X'
  while check_empty_cells_on_field(field):
    render_field(field)
    if is_turn_X:
      player = 'X'
    else:
      player = 'O'
    coordinates = input(f'Ход {player}. Введите координаты (через пробел) -> ')
    turn(field, coordinates, player)
    if check_winner(player, field):
      print(f'\n                             >>> Победил {player} <<<')
      render_field(field)
      break
    is_turn_X = not is_turn_X
  else:
    print('                                         > Ничья <')
    render_field(field)
  
def init():
  field = create_field()
  game(field)

init()