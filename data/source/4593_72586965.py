import sys
from math import sqrt, pi, sin, factorial
from decimal import *

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(x, y):
  s = "RSPR"
  
  for i in range(3):
    if x == s[i] and y == s[i + 1]:
      return True
  
  return False


def solve():
  while 1:
    a = input()
    b = input()
    
    if a == b == "E":
      break
    
    cnt = [0,0]
    
    for i in range(len(a)):
      x = a[i]
      y = b[i]
  
      if x == y:
        continue
      
      if f(x, y):
        cnt[0] += 1
      else:
        cnt[1] += 1

    p("P1:", cnt[0])
    p("P2:", cnt[1])


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
