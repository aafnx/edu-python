	# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

def del_substr(str, substr):
  str = str.split()
  str = list(filter(lambda x: substr not in x, str))
  str = ' '.join(str)
  return str

str = 'Мы неабв очень абв любим Питон иабв Джавабв'

print(del_substr(str, 'абв'))