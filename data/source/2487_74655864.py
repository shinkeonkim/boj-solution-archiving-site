import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta
sys.setrecursionlimit(10**7)

BLANK = " "

# inp = input
inp = lambda : sys.stdin.readline().rstrip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

l = []
cnt = 0
visited = []

def gcd(a, b):
  return gcd(b, a % b) if b > 0 else a

def f(i):
  global visited, cnt, l
  if visited[i]:
    return
  
  cnt += 1
  visited[i] = 1
  f(l[i])
  
  
def solve():
  global l, visited, cnt
  
  n = ii()
  l = mii()
  visited = [0] * n
  
  for i in range(n):
    l[i] -= 1
  
  ans = 1
  for i in range(n):
    cnt = 0
    f(l[i])
    
    if(cnt > 0):
      ans = cnt * ans // gcd(ans, cnt) 
  
  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    
