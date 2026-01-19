for _ in range(int(input())):
  n = int(input())
  
  d = {}
  
  for i in range(1, 11):
    d[i] = 0

  for __ in range(n):
    a, b = map(int, input().split())
    
    d[b] = max(d[b], a)
  
  for i in range(1, 11):
    if d[i] == 0:
      print("MOREPROBLEMS")
      break
  else:
    print(sum(d.values()))
