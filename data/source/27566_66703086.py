r, f = map(int, input().split())

d = (180 * f // r) % 360

if 90 <= d <= 270:
  print("down")
else:
  print("up")