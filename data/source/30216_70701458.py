import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())

n = ii()
l = []
while len(l) < n:
  try:
    _l = mii()
    l.extend(_l)
  except:
    break


ans = 1
crt = 1

for i in range(1, len(l)):
  if l[i - 1] < l[i]:
    crt += 1
  else:
    crt = 1
  
  ans = max(crt, ans)

print(ans)
