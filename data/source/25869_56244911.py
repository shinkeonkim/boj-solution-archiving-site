a, b, c = map(int, input().split())

if a < 2 * c or b < 2 * c:
  print(0)
else:
  print(max((a - 2 * c) * (b - 2 * c), 0))
