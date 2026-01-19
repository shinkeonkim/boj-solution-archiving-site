import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k, i, j = mii()
  
  ans = 0

  # 앞으로 옮겨지지 않은 구간의 합
  
  a, b = i, j

  a -= k
  b -= k
  
  a = max(a, 0)
  b = max(b, 0)
  
  ans += (a + b) * (b - a + 1) // 2

  # 앞으로 옮겨진 구간의 합
  
  a, b = 1, k
  c, d = i, j
  
  
  a, b = max(a, c), min(b, d)
  
  if a <= b:
    diff = n - k
    
    a += diff
    b += diff
    ans += (a + b) * (b - a + 1) // 2
  
  p(ans)

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()