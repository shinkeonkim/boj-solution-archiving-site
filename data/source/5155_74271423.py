import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  n, m = mii() # n: 환자수, m: 기계 수
  machines = [mii() for _ in range(m)]

  ans = []
  cnt = {}
  
  for i in range(1, m + 1):
    cnt[i] = 0
  
  for _ in range(n):
    cnt[ii()] += 1
  
  # 구매비용, 사용비용, 최대 사용 횟수, 금액
  
  for i in range(1, m + 1):
    pc, c, u, r = machines[i - 1]
    
    use_cnt = min(u, cnt[i])
    
    plus = r * use_cnt
    minus = pc + c * use_cnt
    
    if plus > minus:
      ans.append(i)
  
  return ans
  
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    p(f"Data Set {t}:")
    for i in ret:
      p(i)
    p()