import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  # 승점: 2, 무승부: 1, 패배: 0
  A = ii()
  B = ii()
  
  if A % 2 != B % 2:
    p("Error")
    return
  
  if A >= 2 and B >= 2:
    p("Undefined")
    return
  
  print(A // 2)
  print(B // 2)
  print(A % 2)
    

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
