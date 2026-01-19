l = [*map(int, input().split())]

c = 0
for i in range(len(l) // 2):
  if l[i] == l[-(i + 1)]:
    continue
  else:
    c += 1
    l[i] = l[-(i + 1)]

if c > 1:
  print("EI")
else:
  print("JAH")
  print(*l)