a, b = 0, 0
c, d = 0, 0
for i in range(int(input())):
  x, y, z = map(int, input().split())
  a += y
  b += z
  if y > z:
    c += x
  else:
    d += x

s = a + b

if a * 2 > s and c > d:
  print(1)
elif b * 2 > s and d > c:
  print(2)
else:
  print(0)
