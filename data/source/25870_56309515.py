s = input()
d = {}

for i in s:
  if i in d:
    d[i] += 1
  else:
    d[i] = 1

l = list(set([i % 2 for i in d.values()]))

if len(l) == 1:
  print(l[0])
else:
  print(2)
