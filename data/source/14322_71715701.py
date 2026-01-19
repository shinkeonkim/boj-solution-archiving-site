import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  return len(set(list(s.replace(" ", ""))))


def solve():
  n = ii()
  
  ans = input()
  mx = f(ans)
  for _ in range(n - 1):
    s = input()
    crt = f(s)
    if mx < crt:
      mx = crt
      ans = s
    elif mx == crt:
      if ans > s:
        ans = s
  return ans
    
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")
