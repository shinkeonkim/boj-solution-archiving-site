n, m = map(int, input().split())
l = []
for i in range(m):
  input()
  l.append([*map(int, input().split())])

chk = [True] + [False] * n
conditions = [0] * (n + 1)
  
for i in range(m):
  for j in range(1, len(l[i])):
    conditions[l[i][j - 1]] = l[i][j]

ans = True

for i in range(1, n + 1):
  if not chk[conditions[i]]:
    ans = False
    break
  
  chk[i] = True

print("Yes" if ans else "No")
