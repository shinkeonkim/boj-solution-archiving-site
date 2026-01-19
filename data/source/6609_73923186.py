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
  # 알 기간은 하루도 안된다.
  # 나머지는 일주일 걸린다
  
  # 유충으로 일주일
  # 번데기 일주일
  # 성충 일주일
  
  # 일요일마다
    # e개의 알을 낳고 죽는다.
    # 그러고 하루마다 부화. -> e마리 부화
    # 그 다음주 R번째? (R의 배수 번째 인듯?) 가 번데기
    # 그 다음주 S번째 번데기만 살아남아.
  
  while 1:
    try:
      M, P, L, E, R, S, N = mii()
    except:
      break
    
    # M: 모기
    # P: 번데기
    # L: 유충
    
    for _ in range(N):
      _L = M * E
      M = 0

      _P = L // R
      _M = P // S
      
      M = _M
      P = _P
      L = _L
    
    p(M)
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
