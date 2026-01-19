t = [4, 6, 4, 10]
d = {}
for i in range(int(input())):
  l = [input().split() for i in range(4)]
  
  for j in range(4):
    for k in range(len(l[j])):
      if l[j][k] == '-':
        continue
      
      try:
        d[l[j][k]] += t[j]
      except:
        d[l[j][k]] = t[j]

d = d.values()
mn = min(d or [0])
mx = max(d or [0])

print('Yes' if mx - mn <= 12 else 'No')
