import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def g(a):
  return a * a

def f(p1, p2):
  return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def solve():
  points = [mii() for _ in range(3)]
  
  r = fi()
  dis = []
  
  for i in range(3):
    dis.append(f(points[i], points[(i + 1) % 3]))
  
  
  f1 = r * sum(dis) / 2
  
  k1 = 4 * g(dis[0])* g(dis[1])
  k2 = g(g(dis[0]) + g(dis[1]) - g(dis[2]))
  f2 = sqrt(k1 - k2) / 4
  
  p((f2 - f1) / f1 * 100)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
