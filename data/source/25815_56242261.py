y, m = map(int, input().split())

if y == 0:
  a = 0
elif y == 1:
  a = 15
elif y == 2:
  a = 24
else:
  a = 24 + (y - 2) * 4

if y == 0:
  b = 15 * m
elif y == 1:
  b = 9 * m
else:
  b = 4 * m

a += b // 12
b %= 12

print(a, b)