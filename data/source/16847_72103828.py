import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  ans = 0

  n, k = mii()  
  s = inp()
  l = [inp() for _ in range(n)]
  
  for i in range(k):
    for j in range(n):
      if l[j][i] == s[i]:
        break
    else:
      ans += 1
          
  return f"{ans}/{k}"

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"Data Set {t}:")
    p(ret)
    p()
