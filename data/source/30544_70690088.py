import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " ": [*map(int,inp().split(x))]
mfi = lambda x = " ": [*map(float,inp().split(x))]
ii = lambda : int(inp())

h, m = mii(":")
n = ii()

t = h* 60 + m

cnt = 0
while 1:
  if t % 60 == 0:
    k = (t // 60) % 12
    if k == 0:
      k = 12
    cnt += k
  elif t % 15 == 0:
    cnt += 1
  
  if cnt >= n:
    break
  
  t += 1

h = (t // 60) % 12
if h == 0:
  h = 12

print(f"{h:02d}:{t%60:02d}")