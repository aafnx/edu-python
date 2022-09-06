# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#     Найдите произведение элементов на указанных пользователем через пробел позициях.

lst = []
n = 3
rng = range(-n, (n + 1))

for i in (rng):
  lst.append(i)

print(f'Сгенерированный список - {lst}')

position = input('Введите позиции элементов через пробел -> ')

# Сделал так что пользователь пишет не индексы элементов, а их порядковые числа
# то есть с 1 и далее

def pos(position, numbers):
  position_split = position.split()
  position_end = int(position_split[-1])
  if '0' in position_split:
    print('Вы обратились к 0 элементу, такого элемента в списке нет')
    return
  if (position_end > len(numbers)):
    print(f'Вы обратились к элементу {position_end}, но в списке всего {len(numbers)} элементов')
    return
  print(f'Пользователь обратился к позициям - {position_split}')

  res = 1
  numbers_index = []
  for item in position_split:
    item = int(item)
    num = numbers[item - 1]
    res *= num
    numbers_index.append(num)

  print(f'Полученные элементы - {numbers_index}')
  print(f'Произведение полученных элементов - {res}')

pos(position, lst)