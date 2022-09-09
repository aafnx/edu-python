# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).

#     Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_binary_number(n):
  res = ''
  while n >= 2:
    remains = n % 2
    n //= 2
    res += str(remains)
    
  n %= 2
  res += str(n)
  res = int(res[::-1])
  return res

print(get_binary_number(2))
print(get_binary_number(3))
print(get_binary_number(22))
print(get_binary_number(45))