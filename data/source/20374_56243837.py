x = y = 0

while 1:
  try:
    s = input()
  except:
    break
  
  a, b = map(int, s.split("."))
  
  x += a
  y += b

x += y // 100
y %= 100

print(f"{x}.{y:02d}")