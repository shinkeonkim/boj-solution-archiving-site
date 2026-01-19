import sys
from math import sqrt, pi, sin, factorial

BLANK = " "

inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  d = [i for i in range(20000)]
  
  d[0] = d[1] = 0
  
  l = []
  
  for i in range(2, 20000):
    if d[i] == i:
      l.append(i)
      
      for j in range(i + i, 20000, i):
        d[j] = 0
  
  
  for _ in range(ii()):
    k = ii()
    
    print(f"Input value: {k}")
    
    if d[k]:
      print("Would you believe it; it is a prime!")
    else:
      diff = 11111111111111111111
      for i in l:
        if abs(i - k) < diff:
          diff = abs(i - k)
      print(f"Missed it by that much ({diff})!")
    
    p()
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

