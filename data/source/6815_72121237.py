import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  i = 1
  a = ii()
  b = ii()
  
  A = set()
  B = set()

  while i * i <= b:
    if a <= i ** 2 <= b:
      A.add(i * i) 
    if a <= i ** 3 <= b:
      B.add(i ** 3)
    i += 1
  
  print(len(A.intersection(B)))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
