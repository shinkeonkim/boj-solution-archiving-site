import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    D = [0] * 20

    k = input()
    
    if k == '#':
      break
    
    s, *l = k.split()
    chk = 0
    s = int(s) - 1
    D[s] += 1

    for i in l:
      num = int(i[1:])
      if i[0] == 'U':
        s += num
      else:
        s -= num
      
      if s < 0 or s >= 20:
        chk += 1
        break
      
      D[s] += 1
    
    chk += len([i for i in D if i > 1])
    if chk > 0:
      p("illegal")
    else:
      ans = []
      cnt = 0
      for i in range(20):
        if D[i] == 0:
          cnt += 1
          ans.append(i + 1)
      if cnt == 0:
        p("none")
      else:
        p(*ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
