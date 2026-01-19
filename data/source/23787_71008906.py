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
  s_1 = s[0] == '1'
  
  l = []
  crt = ans = 0
  
  for i in s:
    if i == '1':
      if crt > 0:
        if not s_1:
          ans = max(ans, crt)
        else:
          ans = max(ans, (crt + 1) // 2)
        crt = 0
      continue
    if i == '0':
      crt += 1
  if crt > 0:
    ans = max(ans, crt)
  p(ans)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
