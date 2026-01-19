import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  L, R, N, M = mii()
  
  if N == M:
    return "G"
  
  left = abs(N - M) <= L
  right = abs(N - M) <= R
  
  if left and right:
    return "E"
  
  if left:
    return "L"
  
  return "R"
  
  
if __name__ == "__main__":
  tc = ii()
  
  for t in range(1, tc+1):
    p(solve())
