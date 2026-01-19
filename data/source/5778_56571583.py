while 1:
  n, m = map(int, input().split())
  
  if n == 0:
    break
  
  l = [*map(int, input().split())]
  
  d = {}
  
  for i in l:
    if i in d:
      d[i] += 1
    else:
      d[i] = 1
  
  ans = 0
  
  for i in d.values():
    if i > 1:
      ans += 1
  print(ans)