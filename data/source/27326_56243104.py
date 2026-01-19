n = int(input())
l = sorted([*map(int,input().split())])
for i in range(0, (n - 1) * 2, 2):
  if l[i] != l[i + 1]:
    print(l[i])
    break
else:
  print(n)