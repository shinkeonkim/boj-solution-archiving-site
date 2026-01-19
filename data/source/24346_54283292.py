s = input()
d = {}

for i in s:
  try:
    d[i] += 1
  except:
    d[i] = 1

l = list(map(lambda t: t % 2, d.values()))

z = l.count(0)
o = len(l) - z

if z > 0:
  print(1 if o == 0 else o)
else:
  print(o)
