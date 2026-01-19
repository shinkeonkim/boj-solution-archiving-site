n, r = map(int, input().split())

if n > r:
  print(n + 2 * r - 1)
else:
  print(n * ((r // n) * 2 + 1) + ((r % n) * 2) - 1)
