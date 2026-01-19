import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  c, n = mii()
  
  a = mii() # 각 국가에 등록된 선수 수
  b = mii() # 각 선수의 국가 소속
  
  for i in b:
    a[i - 1] -= 1
  
  print(max(a))
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    p(f"Data Set {t}:")
    ret = solve()
    p()
