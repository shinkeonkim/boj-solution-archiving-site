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

def f(speed, read_time, rest_time, page):
  
  cnt_read_time = page // (speed * read_time)
  
  ret = (read_time + rest_time) * cnt_read_time 

  left_page = page % (speed * read_time)

  ret += (left_page + speed - 1) // speed
  if left_page == 0 and page != 0:
    ret -= rest_time
  
  return ret


def solve():
  N, K = mii() # N 페이지의 책,K 마리 소
  
  for i in range(K):
    speed, read_time, rest_time = mii()
    
    total = f(speed, read_time, rest_time, N)
    
    p(ceil(total))
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
