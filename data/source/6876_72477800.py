import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  s = input().replace("-","")

  d = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
  ans = ""

  for i in s:
    if '0' <= i <= '9':
      ans += i
      continue
    for idx, val in enumerate(d):
      if i in val:
        ans += str(idx)
        break

  return ans

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    p(f"{ret[:3]}-{ret[3:6]}-{ret[6:10]}")
