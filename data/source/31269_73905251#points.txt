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
  n = ii()
  
  a = mii()
  b = mii()
  
  #  1 2 3 i번째의 숫자가 
  # i번째 순위의 코드라는ㄳ
  
  # i번째 숫자는 i번째 코드가 얻은 투표수
  
  SCORE = 2
  MEMBER_SCORE = 1
  l = [[a[i], 0, n - i, 0] for i in range(n)]
  
  l.sort(key = lambda t: t[0])
  
  for i in range(n):
    l[i][MEMBER_SCORE] = b[i]
  
  l.sort(key = lambda t: t[MEMBER_SCORE])
  
  
  for i in range(n):
    l[i][SCORE] += i + 1

  l.sort(key=lambda t: (-t[SCORE], -t[MEMBER_SCORE]))

  for i in range(n):
    p(f"{i + 1}. Kod{l[i][0]:02d} ({l[i][SCORE]})")


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
