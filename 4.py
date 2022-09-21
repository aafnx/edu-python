# 4. Реализуйте RLE (загуглить) алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах. Пример: aaabbcf -> a3b2c1f1


src = 'aaabbcfaawwwwwwwwwwwwwwwwwwbbbwwwwwwwwwwwwwwwwwwwwwxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
  
def packing(source):
  coincidences = 1
  source += ' '
  str = ''
  res = ''
  for i in range(len(source)):
    if source[i] == source[i - 1]:
      str = source[i]
      coincidences += 1
    else:
      res += f'{str}{coincidences}'
      str = source[i]
      coincidences = 1
  return res[1:]

def unpacking(source):
  str = ' '
  number = ''
  res = ''
  for i in range(len(source)):
    if not source[i].isdigit():
      str = source[i]
      number = ''
    else:
      number += source[i]
      res += str * int(number)
    if len(number) > 1:
      digit = int(number[:len(number)-1])
      res = res[:len(res) - digit]
  return res


p = packing(src)
print(p)

u = unpacking(p)
print(u == src)
print(packing(u))

    