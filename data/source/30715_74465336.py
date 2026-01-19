import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
# sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

  
def solve():
  n, k, x = mii()
  
  # n : 제시하고 싶은 문제 수
  # k: 상사가 거부할 수 있는 최대 문제 수
  # x: 그리샤에 따른 대회의 최소 허용 난이도
  
  #n - k 개의 합이 x보다 크거나 같아야 한다.
  
  avg = x // (n - k)
  
  if x % (n - k) > 0:
    p(avg * (n - k) + (x % (n - k)) + (avg + 1) * k)    
  else:
    p(avg * n)
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
