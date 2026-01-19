import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(circle, crt):
  return (circle[0]-crt[0])**2 + (circle[1]-crt[1]) ** 2 <= circle[2] ** 2
  
def g(rect, crt):
  return rect[0] <= crt[0] <= rect[2] and rect[1] <= crt[1] <= rect[3]


def solve():
  rects = []
  circles = []
  
  m = ii()
  
  for _ in range(m):
    cat, *l = input().split()
    l = [*map(int, l)]
    
    if cat == "circle":
      circles.append(l)
    else:
      rects.append(l)
  
  for _ in range(ii()):
    crt = mii()

    cnt = 0
    for circle in circles:
      cnt += 1 if f(circle, crt) else 0
    for rect in rects:
      cnt += 1 if g(rect, crt) else 0
    p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
