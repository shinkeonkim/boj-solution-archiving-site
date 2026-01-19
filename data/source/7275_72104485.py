import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,input().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, k, m = mii() # n 옷 색상 수, k: 옷 그룹 수, m: 세탁기 용량
  
  groups = [mii()[1:] for _ in range(k)]  
  cnt = mii()
  ans = 0

  for group in groups:
    c = 0
    for cloth in group:
      c += cnt[cloth - 1]
      cnt[cloth - 1] = 0
    
    ans += c // m + int(c % m > 0)

  for c in cnt:
    ans += c // m + int(c % m > 0)

  print(ans)
  

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
