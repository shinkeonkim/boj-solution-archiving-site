n, m = map(int, input().split())
l = [[*map(int, input().split())] for i in range(n)]

d = {}

for _ in range(n):
  for i in range(m):
    if l[_][i] == 1:
      d[i] = d.get(i, 0) + 1

d = sorted(d.items(), key = lambda t : (-t[1], t[0]))

for i, _ in d:
  print(i + 1, end = " ")