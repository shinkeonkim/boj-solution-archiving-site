import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  K = ii() # 셀 크기
  W = ii()
  H = ii()
  T = ii() # 선 두께

  for h in range(H):
    for _ in range(T):
      print("*" * (W * (K + T) + T))
    for k in range(K):
      print(("*" * T + "." * K) * W + "*" * T)

  for _ in range(T):
    print("*" * (W * (K + T) + T))

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    # p(ret)