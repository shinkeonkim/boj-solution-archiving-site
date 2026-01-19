l = sorted([*map(int, input().split())])

if l[0] == 0:
  if l[1] == 0:
    print(l[2], 0, 0, sep="")
  else:
    print(l[1], l[0], l[2], sep="")
else:
  print(*l, sep="")