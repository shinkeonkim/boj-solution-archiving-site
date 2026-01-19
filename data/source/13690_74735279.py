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
    s = input()
    
    if s == "0 0 0":
      break
      
    V, N, M = s.split()
    V = float(V) # 배팅값
    
    N = int(N)
    M = int(M)
    
    ret = 0
    if M % 10000 == N % 10000:
      ret = V * 3000 # 받는다
    elif M % 1000 == N % 1000:
      ret = V * 500
    elif M % 100 == N % 100:
      ret = V * 50
    else:
      a = (N % 100 - 1) // 4
      b = (M % 100 - 1) // 4
      
      if a == b:
        ret = V * 16
    
    p(f"{ret:.2f}")
    
    
    
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
