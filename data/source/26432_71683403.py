import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  m, n, p = mii() # 참가자 수, 총 일수, 작년 참가 ID

  d = [mii() for _ in range(m)]

  ans = 0

  for i in range(n):
    k = max([d[j][i] for j in range(m)])
    ans += abs(d[p - 1][i] - k)

  return ans

if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()

    print(f"Case #{t}: {ret}")