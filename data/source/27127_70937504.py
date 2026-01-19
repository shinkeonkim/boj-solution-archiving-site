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
  
  l = []
  
  for i in range(10000, 100000):
    if i % 9:
      continue
    
    j = i // 9
    
    a = str(i)
    b = str(j)
    
    if j <= 9999:
      b = "0" + b

    z = set(list(a + b))
    
    if len(z) != 10:
      continue
    
    l.append([a, b])
    
  print(*l[n-1])
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
