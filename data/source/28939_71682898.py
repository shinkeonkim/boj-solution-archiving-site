import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  k, m1, m2 = mii()
  l = [mii() for _ in range(n)]
  ans = 0
  for i in range(n):
    h, s, *sizes = l[i] # 선반 높이, 신발 수, 신발 크기들?

    for size in sizes:
      a = (h, h * k)
      b = (size * m2, size * m1)
      
      if b[1] < a[0] or a[1] < b[0]:
        ans += 1
  print(ans)      
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
    # p(ret)
