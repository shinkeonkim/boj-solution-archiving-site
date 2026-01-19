while 1:
  try:
    l = [*map(int, input().split())]
    d = [0] * len(l)
    
    for i in range(len(l)):
      d[i] = l[i]
      if i > 0:
        d[i] *= l[i - 1]
      if i + 1 < len(l):
        d[i] *= l[i + 1]
    print(*d)
  except:
    break