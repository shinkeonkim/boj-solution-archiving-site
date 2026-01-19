n = int(input())
l = [input() for i in range(n)]

mx = max([len(i) for i in l])

for i in range(mx):
  d = {}
  
  for j in range(n):
    if i >= len(l[j]):
      continue

    try:
      d[l[j][i]] += 1
    except:
      d[l[j][i]] = 1
  
  d = sorted(d.items(), key = lambda t : (-t[1], t[0]))
  
  mx_cnt = max([item[1] for item in d])
  
  print(end=f'{i + 1}: ')
  for c, cnt in d:
    if cnt == mx_cnt:
      print(c, end=" ")
    else:
      break
  print()
  