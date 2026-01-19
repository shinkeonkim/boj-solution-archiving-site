def f(p):
  d = [-1, 4, 11, 23, 40, 60, 77, 89, 96, 100]

  for i in range(10):
    if p <= d[i]:
      return i

N, K = map(int, input().split())
l = [*map(int, input().split())]

for i in l:
  print(f(i * 100 // N), end=" ")