import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(i):
  if '0' <= i <= '9':
    return int(i)
  
  return ord(i) - 55

def solve():
  s = input()
  score = 0
  week = 0
  ext = ""
  
  d = [0, 1, 1, 1, 1, 1]

  for i in s:
    i = f(i)
    
    score += i
        
    if score // 10 > 4:
      p(f"{week}(09)")
      return
    
    if score // 10 == 4:
      p(f"{week}(weapon)")
      return
    week += d[score // 10] * (score // 10)
    d[score // 10] = 0
  
  p(f"{week}")
    
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
