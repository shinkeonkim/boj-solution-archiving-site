for _ in range(int(input())):
  n = int(input())
  l = [*map(int, input().split())]
  
  d = l.count(2)
  
  if d % 2 == 1:
    print(-1)
    continue
    
  d //= 2
  
  c = 0
  for idx, i in enumerate(l):
    if i == 2:
      c += 1
      
    if c == d:
      print(idx + 1)
      break
  