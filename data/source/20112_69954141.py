n = int(input())
l = [input() for i in range(n)]

chk = True

for i in range(n):
  for j in range(n):
    if l[i][j] != l[j][i]:
      chk = False

print("YES" if chk else "NO")