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
  while 1:
    n = ii()
    
    if n == 0:
      break
    
    d = {}
    
    cnt = [{}, {}, {}]
    for _ in range(n):
      k, *l = mii()
      
      for i in range(k):
        d[l[i]] = d.get(l[i], 0) + (3 - i)
        
        cnt[i][l[i]] = cnt[i].get(l[i], 0) + 1
    
    mx = max(d.values())
    
    ans = []
    
    l = []
    for k, v in d.items():
      l.append([k, v, cnt[0].get(k, 0), cnt[1].get(k, 0), cnt[2].get(k, 0)])
    
    l.sort(key = lambda t:(-t[1], -t[2], -t[3], -t[4]))
    
    ans.append(l[0][0])
    
    for i in range(1, len(l)):
      if l[i][1:] == l[0][1:]:
        ans.append(l[i][0])
    
    p(*sorted(ans))
    
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
