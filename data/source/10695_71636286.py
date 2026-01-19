import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, a, b, y, x = mii()
  
  dy = [-1, -1, 1, 1, -2, -2, 2, 2]
  dx = [2, -2, 2, -2, 1, -1, 1, -1]
  
  for i in range(8):
    ny = a + dy[i]
    nx = b + dx[i]

    if ny < 1 or nx < 1 or ny > n or nx > n:
      continue

    if ny == y and nx == x:
      return True
      
  return False
    

if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    ret = solve()
    
    k = "YES" if ret else "NO"
    print(f"Case {t}: {k}")