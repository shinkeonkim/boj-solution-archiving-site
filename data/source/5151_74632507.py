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
  n, m, T = mii() # n: 국회의원, m: 기부자 수, T: 투표 시간(일)
  
  donations = [input().split() for _ in range(m)]
  chk = [input() for _ in range(n)]
  
  d = {}
  
  for a, t, money in donations:
    a = int(a)
    t = int(t)
    money = float(money)
    
    if 0 <= T - t < 1000:
      d[a] = d.get(a, 0) + money

  Y, N = 0, 0
  
  for i in range(n):
    D = d.get(i + 1, 0)
    k = 1 / (1 + D / 10000)
    
    if chk[i] == 'Y':
      Y += 1
    else:
      N += k
  return (Y, N)
      
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    p(f"{ret[0]:.2f} {ret[1]:.2f}")
    p()
    
