import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s, n):
  ret = 0
  for i in range(10):
    k = 0    
    if s[i] == '?':
      k = n
    elif s[i] == 'X':
      k = 10
    else:
      k = int(s[i])
    
    ret += k * (10 - i)
  return ret

def solve():
  s = input()
  idx = -1
  sm = 0
  
  for i in range(10):
    if s[i] == '?':
      idx = i
      continue
  
  k = 10
  if idx == 9:
    k = 11

  for i in range(k):
    k = f(s, i)
    
    if k % 11 == 0:
      if i == 10:
        p("X")
      else:
        p(i)
      return
  p(-1)
  
    
        
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()

    