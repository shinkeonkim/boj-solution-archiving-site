import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
  

def solve():
  n = ii()
  idx = [0] * n
  l =[]
  for _ in range(n):
    _, *_l = mii()
    l.append(_l)
  
  while 1:
    k = -1
    z = 1000000000
    for i in range(n):
      if idx[i] >= len(l[i]):
        continue
      
      if z > l[i][idx[i]]:
        z = l[i][idx[i]]
        k = i

    if k == -1:
      break
    
    idx[k] += 1
    print(end=chr(k + 65))
  
  

if __name__ == "__main__":
  tc = 1
  for t in range(tc):
    solve()
    