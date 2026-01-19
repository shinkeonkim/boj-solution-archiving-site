for i in range(int(input())):
  l = [*map(int, input().split())]
  
  t = 0
  
  if l[0] + l[1] + l[2] > l[3] + l[4] + l[5]:
    t |= 1
  
  if l[0] > l[3]:
    t |= 2
  elif l[0] == l[3]:
    if l[1] > l[4]:
      t |= 2
    elif l[1] == l[4]:
      if l[2] > l[5]:
        t |= 2
  
  print(*l)
  print(["none", "count", "color", "both"][t])
  print()
