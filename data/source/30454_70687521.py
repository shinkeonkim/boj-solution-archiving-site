import sys
from math import sqrt, pi, sin
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())


N, L = mii()
l = [input() for i in range(N)]

mx = 0
ans = 0

for s in l:
  cnt = 0
  stat = False

  for j in s:
    if j == '1':
      stat = True
    else:
      if stat:
        cnt += 1
      stat = False
  if stat:
    cnt += 1
  
  if mx < cnt:
    mx = cnt
    ans = 1
  elif mx == cnt:
    ans += 1
print(mx, ans)