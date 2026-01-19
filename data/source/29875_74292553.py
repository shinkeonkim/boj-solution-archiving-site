import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = mii()
  # 빨강 O -> 버튼(0, 1) -> 녹색 ON
  # 녹 -> 0 -> 빨
  # 녹 -> 1 -> 파
  
  # 파 -> 0 -> 노
  # 파 -> 1 -> 파
  
  # 노 -> 0 -> 노
  # 노 -> 1 -> 빨
  
  statuses = [1]
  
  for k in l:
    ls = []
    
    if k == -1:
      ls.extend([0, 1])
    else:
      ls.append(k)
    
    z = []
    
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    
    for i in ls:
      for status in statuses:
        ret = status

        if status == RED:
          if i == 0 or i == 1:
            ret = 2
        elif status == GREEN:
          if i == 0:
            ret = RED
          elif i == 1:
            ret = BLUE
        elif status == BLUE:
          if i == 0:
            ret = YELLOW
          elif i == 1:
            ret = BLUE
        elif status == YELLOW:
          if i == 0:
            ret = YELLOW
          elif i == 1:
            ret = RED
        z.append(ret)
    statuses = [*set(z)]
  
  for i in range(1, 5):
    if i in statuses:
      p("JAH")
    else:
      p("EI")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
