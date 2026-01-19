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
  s = input()
  n = len(s)
  idx = 0
  for i in range(n):
    if s[i] == '0' or s[i] == '1':
      idx = i
  
  logic_cnt = idx
  fact_cnt = n - idx - 1
  
  num = 1 if fact_cnt > 0 else int(s[idx])
  
  if logic_cnt % 2:
    num = 1 - num
  
  p(num)
  
      
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
