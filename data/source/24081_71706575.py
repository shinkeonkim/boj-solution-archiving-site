import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m = mii()
  box = sorted(mii())
  key = sorted(list(set(mii())))
  
  i = j = 0
  ans = 0

  while i < len(box) and j < len(key):
    if box[i] == key[j]:
      ans += 1
      i += 1
    elif box[i] < key[j]:
      i += 1
    else:
      j += 1
  return ans
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)
