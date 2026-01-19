n = int(input())
l = [*map(int, input().split())]

d = {}

for i in l:
  if i == 0:
    continue
  d[i] = d.get(i, 0) + 1


if len(d) == 0:
  print("skipped")
else:
  l = sorted(d.values(), key = lambda t : -t)
  
  if l.count(l[0]) > 1:
    print("skipped")
  else:
    for k, v in d.items():
      if v == l[0]:
        print(k)
        break