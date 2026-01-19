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
    n, m, p = mii()
    
    if n == m == p == 0:
      break
    
    l = [ii() for _ in range(n)]
    
    c = l[m - 1] # 돈 딴 사람 수
    
    total_money = sum(l) * (100 - p)
    
    print(total_money // c if c > 0 else 0)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

