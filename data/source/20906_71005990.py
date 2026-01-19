import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  t, s , n = mii()
  l = mii()
  
  fall = s
  prev = 0
  for i in l:
    time = i - prev
    fall += min(time, s)
    fall = min(fall, s)
    fall = s - fall
    prev = i
    
  k = max(0, s - fall - (t - prev))
  print(k)
      
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
