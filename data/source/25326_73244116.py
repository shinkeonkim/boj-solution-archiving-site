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

def f(s):
  return s[0]

def solve():
  n, m = mii()
  l = [[*map(f, input().split())] for _ in range(n)]
  
  for _ in range(m):
    q = [*map(f, input().split())]
    ans = 0
    for i in l:
      cnt = 0
      for idx in range(3):
        if q[idx] == '-':
          cnt += 1
        elif q[idx] == i[idx]:
          cnt += 1
      if cnt == 3:
        ans += 1
    p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
