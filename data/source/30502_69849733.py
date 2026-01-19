N, M = map(int, input().split())

chk = [[2] * 2 for i in range(N)]

for _ in range(M):
  a, b, c = input().split()
  a = int(a)
  c = int(c)
  
  chk[a - 1][{'P': 0, 'M': 1}[b]] = c

mn = 0
mx = 0
for i in range(N):
  if chk[i][0] == 0 or chk[i][1] == 1:
    continue
  
  if chk[i][0] == 1 and chk[i][1] == 0:
    mn += 1
    mx += 1
  else:
    mx += 1
print(mn, mx)
