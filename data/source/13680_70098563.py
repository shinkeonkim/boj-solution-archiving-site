while 1:
  a, b, x, y = map(int, input().split())
  
  if a == b == x == y == 0:
    break

  m = min(abs(a - x), abs(b - y))
  
  print(int(abs(a - x) - m > 0) + int(abs(b - y) - m > 0) + int(m > 0))