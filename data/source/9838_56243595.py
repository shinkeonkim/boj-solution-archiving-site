d = {}
for i in range(int(input())):
  a = int(input())
  d[a] = i + 1

d = sorted(list(d.items()), key = lambda t : t[0])

for i, j in d:
  print(j)