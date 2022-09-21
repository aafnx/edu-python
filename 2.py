# 2. Создайте программу для игры с конфетами человек против человека.
# 		Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет (не менее 1). Все конфеты оппонента достаются сделавшему последний ход.
# 		a)* Добавьте игру против бота
# 		b)* Подумайте как наделить бота ""интеллектом""

import random

def check_count_entered_candies(count):
  if 1 <= count <= 28:
    return True
  return False

def player_turn(player, all_candies):
  candies = 0
  player_name = player['name']
  while True:
    candies = int(input(f'{player_name} - Введите количество конфет от 1 до 28 -> '))
    if check_count_entered_candies(candies) and (candies <= all_candies):
      break
    else:
      print(f'{player_name} ввел некорректное значение, нужно от 1 до 28, или вы ввели больше чем осталось конфет - {all_candies}')
  player['candies'] += candies
  return candies

def set_player_win(player_winner, player_loose):
  player_winner['candies'] += player_loose['candies']
  player_winner['winner'] = True
  player_winner_name = player_winner['name']
  player_winner_candies = player_winner['candies']
  player_loose_name = player_loose['name']
  player_loose_candies = player_loose['candies']
  player_loose['candies'] = 0
  print(f'Победил игрок - {player_winner_name}, он забирает  {player_loose_candies} конфет у игрока {player_loose_name}')


def create_player(name):
  return {'name': name, 'candies': 0,'winner': False}

def turn_draw():
  turn = random.randint(1, 2)
  is_turn_player_1 = False
  if turn == 1:
    is_turn_player_1 = True
  return is_turn_player_1

def game(candies, player_1, player_2, is_turn_player_1, is_game_bot):
  print(f'Всего конфет - {candies}')
  while candies > 0:
    current_candies = 0
    if is_game_bot:
      current_candies = player_turn(player_1, candies) if is_turn_player_1 else bot(candies, player_2)
    else:
      current_candies = player_turn(player_1, candies) if is_turn_player_1 else player_turn(player_2, candies)

    candies -= current_candies
    if candies == 0:
      set_player_win(player_1, player_2) if is_turn_player_1 else set_player_win(player_2, player_1)
      return
    print(f'Конфет осталось - {candies}')
    is_turn_player_1 = not is_turn_player_1

def init(candies):
  candies = candies
  player_1 = create_player('Player 1')
  play_bot = input('Если хотите сыграть с ботом введите (y) - ')
  is_game_bot = False
  if 'y' in play_bot:
    player_2 = create_player('BOT')
    is_game_bot = True
  else:
    player_2 = create_player('Player 2')
  is_turn_player_1 = turn_draw()
  game(candies, player_1, player_2, is_turn_player_1, is_game_bot)

def bot(candies, bot):
  bot_name = bot['name']
  i = 0
  while True:
    value_candies = random.randint(1, 28)
    if candies <= 28:
      value_candies = 28 - i
    elif candies <= 56:
      value_candies = candies - 29 + i
    if check_count_entered_candies(value_candies) and (value_candies <= candies):
      break
    i += 1
  print(f'{bot_name} - Взял {value_candies} конфет ')
  bot['candies'] += value_candies
  return value_candies


init(100)