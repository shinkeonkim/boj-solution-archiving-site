import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


M, N = mii()
weights = sorted(mii(), reverse=True)
ans = 0


chk = [False] * 4
for _ in range(4):
  cnt = 0
  crt_w = 0
  for i in range(4):
    w = weights[i]
    
    if chk[i]:
      continue

    if cnt + 1<= M and crt_w + w <= N:
      cnt += 1
      crt_w += w
      chk[i] = True
  ans += 1
    
  c = list(set(chk))
  if len(c) == 1 and c[0] == True:
    break
print(ans)