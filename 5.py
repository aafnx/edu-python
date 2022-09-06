# 5. Реализуйте алгоритм перемешивания списка.

lst = []
n = 10
rng = range(-n, (n + 1))

for i in (rng):
    lst.append(i)

print(f'Сгенерированный список - {lst}')


# Получаем числа на основе ссылок на списки
def shuffle_list(source_list: list) -> list:
  new_list = []

  for i in range(len(source_list)):
      a = i
      temporary_list = []  # создаем временный список для получения новой ссылки
      link_num = id(temporary_list)
      divider = 0

      if i % 2 == 0: # если i четное, то генерируем таким способом число
        link_num = id(temporary_list) // 100000 % 3.141592653589793238462643383 + i
        link_num = str(link_num)
        divider = int(link_num[-1])

      else: # иначе другим
        link_num = id(temporary_list) // 100000 % 2.7182818284 - i
        link_num = str(link_num)
        divider = int(link_num[-1])
      
      idx = divider - len(new_list) % (a + 1)  # получаем число

      while (source_list[idx:idx+1] in new_list) or (idx > len(source_list)):
          # пока текущее значение уже есть в новом списке
          # или новый индекс выходит за границы исходного списка
          new_temporary_list = []  # создаем временный список для получения новой ссылки
          link_num = str(id(new_temporary_list))
          link_num = int(link_num[divider+a])
          idx = link_num - len(new_list) # получаем новый индекс
          del new_temporary_list # удаляем список, чтобы не занимать место в памяти
          a += 1
          
      new_list.append(source_list[idx])
      del temporary_list

  return new_list


print(f'Через мой алгоритм - {shuffle_list(lst)}')

## Получаем рандомное число на основе времени

import datetime

new = []
for i in range(len(lst)):
  now = datetime.datetime.now()
  idx = now.microsecond % 10
  while (lst[idx:idx] in new) or (idx > len(lst)):
    now = datetime.datetime.now()
    idx = now.microsecond % 10
  new.append(lst[idx])

print(f'На основе времени - {new}')


# через рандомное число, полученное через random

import random

new = []
for i in range(len(lst)):
  idx = random.randint(0, len(lst)-1)
  while lst[idx] in new:
    idx = random.randint(0, len(lst)-1)
  new.append(lst[idx])

print(f'Через рандомное число - {new}')


# Перемешивание через встроенный функционал

import random

random.shuffle(lst)

print(f'Встроенный функционал - {lst}')
