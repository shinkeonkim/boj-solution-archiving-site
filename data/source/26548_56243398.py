from math import sqrt

def f(a, b, c):
  m = 2 * a
  n = sqrt(b * b - 4 * a * c)
  return ((-b + n) / m, (-b - n) / m)

for i in range(int(input())):
  a, b, c = map(float,input().split())
  x, y = f(a, b, c)
  print(f"{x:.3f}, {y:.3f}")
