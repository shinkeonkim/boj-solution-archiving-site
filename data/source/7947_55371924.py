for tc in range(int(input())):
  a, b, c = 0, 0, 0
  for _ in range(10):
    x, y, z = map(int, input().split())
    
    a += x
    b += y
    c += z
    
  print((a + 5) // 10, (b + 5) // 10, (c + 5) // 10)
