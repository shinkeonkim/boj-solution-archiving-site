import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  E, L, B = mii()
  l = [ii() for _ in range(B)]
  
  INF = 1111111111111111111
  D = [INF] * 44000
  
  chk = [0] * 44000
  
  for i in l:
    chk[i] = 1
  
  D[0] = 0
  
  for i in range(1, E + 1):
    if chk[i]:
      continue
    
    for j in range(1, L + 1):
      D[i] = min(D[i - j] + 1, D[i])
    
  print(D[E])
  
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()

    