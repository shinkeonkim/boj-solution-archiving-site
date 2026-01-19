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
  
  d = {}
  
  for i in s:
    d[i] = d.get(i, 0) + 1
  
  odd_cnt = 0
  
  for v in d.values():
    if v % 2 == 1:
      odd_cnt += 1
  
  print(max(odd_cnt - 1, 0))
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

