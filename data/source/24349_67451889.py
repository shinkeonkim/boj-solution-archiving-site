import sys

n, a, b, c = map(int, input().split())

if n == 1:
  print(0, 0)
  sys.exit()

n -= 1

cm = 0

if a <= b and a <= c:
  cm = a * n
elif b <= c and b <= a:
  cm = b * n
else:
  cm = min(a, b) + c * (n - 1)

print(cm // 100, cm % 100)