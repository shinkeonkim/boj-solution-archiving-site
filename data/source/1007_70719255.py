import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def dis(a):
  return sqrt(a[0]*a[0] + a[1]*a[1])

def solve():
  n = ii()
  points = [mii() for _ in range(n)]
  ans = 111111111111111111111111
  
  for j in range(0, 2 ** n):
    z = [0, 0]
    k = bin(j)[2:]
    k = "0" * (n - len(k)) + k
    if k.count("1") != k.count("0"):
      continue
      
    for i in range(n):
      if k[i] == '1':
        z[0] += points[i][0]
        z[1] += points[i][1]
      else:
        z[0] -= points[i][0]
        z[1] -= points[i][1]
    ans = min(ans, dis(z))
  print(ans)
  
if __name__ == "__main__":
  tc = ii()
  for t in range(tc):
    solve()
    