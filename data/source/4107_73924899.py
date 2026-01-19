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


def solve():
  while 1:
    N, M, K = mii()
    
    # N: 첫번째 행의 침 수
    # M: 전체 행 수
    # K: 반복되는 패턴의 행수???
    
    if N == M == K == 0:
      break
    
    k = mii()
    
    crt = N
    s = N
    for idx in range(M - 1):
      i = idx % K      
      crt += k[i]
      s += crt
      
    p(s)
        
    
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
