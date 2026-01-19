import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k, t = mii() # k는 기다리는 시간, t는 소포 전달 시간
  
  z = mii() # 사무실에서 수취인에게 도달하는데 걸리는 시간
  s = mii() # 수취인이 나타나는 시각
  
  crt = 0
  for i in range(n):
    crt += z[i]
    
    if crt >= s[i]:
      crt += t
    elif crt + k >= s[i]:
      crt = min(crt + k, s[i]) + t
    else:
      crt += k
  
  p(crt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    
