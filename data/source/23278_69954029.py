N, L, H = map(int, input().split())
l = sorted([*map(int, input().split())])

s = []

if H == 0:
  s = l[L:]
else:
  s = l[L:-H]

print(sum(s) / len(s))