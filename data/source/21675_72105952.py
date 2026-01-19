import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  w, h = mii()
  A = [input() for _ in range(h)]
  B = [input() for _ in range(h)]
  
  D = input()
  
  for i in range(h):
    for j in range(w):
      p(D[int(A[i][j]) * 2 + int(B[i][j])],end="")
    print()

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
