import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def solve():
  n, a, b = mii()
  
  # n 전체 사람 수
  # a: 해결 방법 안다
  # b: 더러워 이걸 왜함.
  
  mx = min(n - b, a)
  mn = max(a - b, 0)
  
  print(mn, mx)
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(tc):
    solve()
    