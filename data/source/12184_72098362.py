import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n = ii()
  l = mii()
  p = ii()
  c = [ii() for _ in range(p)]
  
  ans = []
  for target in c:
    cnt = 0
    for i in range(n):
      if l[i * 2] <= target <= l[i * 2 + 1]:
        cnt += 1
    ans.append(cnt)
  return ans
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    print(end=f"Case #{t}: ")
    print(*ret)
    if t + 1 <= tc:
      input()
