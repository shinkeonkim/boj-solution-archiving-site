x, y = map(int, input().split())

if y > x:
  y -= x
  y %= 2 * x
else:
  y += x

print(y)
