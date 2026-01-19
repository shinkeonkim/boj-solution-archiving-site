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

def a(H, P, day):
  total_h = H * day
  price = 5

  cnt = total_h // 1000 + int(total_h % 1000 > 0)
  cost = price * cnt
  
  E = 60
  
  K = E * total_h * P / 100000
  
  return cost + K
  
def b(H, P, day):
  total_h = H * day
  price = 60

  cnt = total_h // 8000 + int(total_h % 8000 > 0)
  cost = price * cnt
  
  E = 11
  
  K = E * total_h * P / 100000
  
  return cost + K


def solve():
  H, P = mii()
  
  for d in range(1, 10000000):
    A = a(H, P, d)
    B = b(H, P, d)
    
    if A > B:
      p(d)
      break
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
