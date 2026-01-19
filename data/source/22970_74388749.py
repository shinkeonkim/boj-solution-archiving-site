import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = mii()
  
  if n == 1:
    p(1)
    return
  
  sign = []
  
  for i in range(1, n):
    if l[i] < l[i - 1]:
      sign.append(-1)
    elif l[i] > l[i - 1]:
      sign.append(1)
    else:
      sign.append(0)
  
  crt = sign[0]
  cnt = 1
  l2 = []
  mx = 1

  for i in sign[1:]:
    if crt == i:
      cnt += 1
    else:
      l2.append([crt, cnt])
      crt = i
      cnt = 1
  l2.append([crt, cnt])
  
  
  for i, cnt in l2:
    if i in [1, -1]:
      mx = max(mx, cnt + 1)
  
  
  for i in range(1, len(l2)):
    prev = l2[i - 1]
    crt = l2[i]
    
    if prev[0] == 1 and crt[0] == -1:
        mx = max(mx, 1 + prev[1] + crt[1])
    
  p(mx)
  
  
tc = 1

for t in range(1, tc+1):
  ret = solve()