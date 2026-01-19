l = sorted([int(input()) for i in range(4)])
b = int(input())

if len(set(l)) == 1:
  print(1)
else:
  l[0] += b
  if len(set(l)) == 1:
    print(1)
  else:
    print(0)
