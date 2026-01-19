d = {}

for i in range(int(input())):
  s=input()
  try:
    d[s] += 1
  except:
    d[s] = 1

l = sorted(list(d.items()), key=lambda t: (-t[1], t[0]))

for i in l:
  if l[0][1] == i[1]:
    print(i[0])
