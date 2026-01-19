import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  s = input()
  n = len(s)
  
  a, b = mii()
  a -= 1
  b -= 1
  
  _a = a % n
  _b = b % n
  
  cnt = 0

  while _a < n and a <= b:
    if s[_a] == 'B':
      cnt += 1
    _a += 1
    a += 1
  
  while _b >= 0 and a <= b:
    if s[_b] == 'B':
      cnt += 1
    _b -= 1
    b -= 1
    
  if a <= b:
    cnt += s.count("B") * ((b - a + 1) // n)
  
  return cnt


if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Case #{t}: {ret}")
