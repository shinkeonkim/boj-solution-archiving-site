import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def lis_idx(n, l):
  if n == 0:
    return []

  track = [i for i in range(n)]
  cnt = [1 for i in range(n)]

  for i in range(n):
    for j in range(i + 1, n):
      if l[i] < l[j] and cnt[i] + 1 > cnt[j]:
        cnt[j] = cnt[i] + 1
        track[j] = i
    
  idx = cnt.index(max(cnt))
  ans = [idx]
  
  while idx != track[idx]:
    idx = track[idx]
    ans.append(idx)
  
  return ans[::-1]

def solve():
  n = ii()
  l = sorted(mii())
  
  k = lis_idx(n, l)
  
  ans = len(k)
  
  l2 = []
  
  j = 0
  for i in range(n):
    if j < len(k):
      if k[j] == i:
        j += 1
        continue
    l2.append(l[i])
  
  ans += len(lis_idx(len(l2), l2))

  p(ans)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
