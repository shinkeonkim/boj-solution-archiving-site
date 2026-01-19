while 1:
  n, m = map(int, input().split())
  
  if n == m == 0:
    break
  
  l = []
  
  for i in range(m):
    l.append([*map(int, input().split())])
    
  ans = 0
  
  for i in range(n):
    d = 0
    
    for j in range(m):
      d += l[j][i]
    ans = max(ans, d)
  print(ans)