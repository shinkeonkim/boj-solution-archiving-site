import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(l):
  ret = []
  
  for i in range(len(l)):
    ret.append(abs(l[i] - l[(i + 1) % len(l)]))
  
  return ret

def solve():
  t = 0
  while 1:
    t += 1

    n = ii()
    if n == 0:
      break
    l = mii()
    
    for _ in range(1000):
      if len(set(l)) == 1:
        p(f"Case {t}: {_} iterations")
        break
      l = f(l)
    else:
      p(f"Case {t}: not attained")
      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

