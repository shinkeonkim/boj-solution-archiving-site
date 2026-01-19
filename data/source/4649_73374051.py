import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    k = input()
    
    if k == "0":
      break
    
    n, s = k.split()
    n = int(n)
    
    ans = 0
    crt = 0
    d = {}
    
    for i in s:
      stat = d.get(i, 0)
      d[i] = stat
      
      if stat == -1:
        continue
      
      if stat == 1:
        d[i] = 0
        crt -= 1
      else:
        if crt + 1 <= n:
          crt += 1
          d[i] = 1
        else:
          ans += 1
          d[i] -= 1
    if ans == 0:
      p("All customers tanned successfully.")
    else:
      p(f"{ans} customer(s) walked away.")

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
