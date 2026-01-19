import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  while 1:
    l = mii()
    
    if sum(l) == 0:
      break
    
    R0, W0, C, R = l
    for x in range(0, 100000):
      if x * R >= W0 * C - R0:
        print(x)
        break
    
    # W0 리터의 물에 R0 그램
    # R 그램에 농도를 C로 만들려한다.
    
    # 농도  (R0 + X * R) / (W0 + )
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
