while 1:
  l = [input() for i in range(int(input()))]
  
  if len(l) == 0:
    break
  print(*l[::-1],sep="\n")
  print(0)