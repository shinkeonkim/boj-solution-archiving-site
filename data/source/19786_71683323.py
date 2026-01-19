import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(A, C, l):
  return A * sum([i * i for i in l]) + C * min(l)

def solve():
  A, C = mii()
  l = mii()

  g = []
  for i in range(3):
    l2 = l[:]
    l2[i] += 1

    g.append(f(A, C, l2))

  print(["RED", "GREEN", "BLUE"][g.index(max(g))])    

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    solve()