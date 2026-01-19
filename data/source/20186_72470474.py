import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k = mii()
  l = mii()
  
  chk = [False] * n
  
  for _ in range(k):
    mx = -9999999
    idx = -1    

    for i in range(n):
      if chk[i]:
        continue

      if mx < l[i]:
        mx = l[i]
        idx = i
    chk[idx] = True
    
  ans = 0
  cnt = 0
  for i in range(n):
    if chk[i]:
      ans += l[i] - cnt
      cnt += 1
  p(ans)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

