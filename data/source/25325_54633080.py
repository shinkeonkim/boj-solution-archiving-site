n = int(input())
l = input().split()
d = {}
for i in l:
  d[i] = 0

for i in range(n):
  l = input().split()
  for j in l:
    d[j] += 1

for k, v in sorted(list(d.items()), key=lambda t: (-t[1], t[0])):
  print(k, v)
