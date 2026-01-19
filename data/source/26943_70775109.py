import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())


def solve():
  n, k = mii()
  d1 = [i for i in range(1, n // 2 + 1)]
  d2 = [i for i in range(n - 1, n // 2, -1)]

  for _ in range(k - 1):
    d2.append(d1.pop())
    d1 = [d2.pop(0)] + d1
      
  d2 = [n] + d2

  for i in range(n // 2):
    print(f"{d1[i]}-{d2[i]}")
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    