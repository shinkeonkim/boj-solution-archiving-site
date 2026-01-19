n = int(input())
l = [*map(int, input().split())]

chk = True

for i in range(n):
  for j in range(n):
    if i == j:
      continue
    for k in range(n):
      if i == k or j == k:
        continue
      if (l[i] - l[j]) % l[k] != 0:
        chk = False

print("yes" if chk else "no")