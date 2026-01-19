import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  tm = [-20] * 9 
  score = [0, 0]
  
  for _ in range(n):
    t, a, b = mii()
    
    if a <= 4:
      if t - tm[a] <= 10:
        score[0] += 50
      score[0] += 100
      tm[a] = t
    else:
      if t - tm[a] <= 10:
        score[1] += 50
      score[1] += 100
      tm[a] = t
  print(*score)
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
