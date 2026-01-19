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
  while 1:
    library, f = input().split()

    if library == '#' and f == '0':
      break

    f = int(f)
    n = ii()
    
    l = [input().split() for _ in range(n)]
    
    # f: 단일 문자의 너비
    # w(책 너비), 텍스트
    # 글자 사이에는 1mm
    # f * len(txt[1])
    
    p(library, "Library")
    for idx in range(n):
      w, txt = l[idx]
      w = int(w)
      
      ln = len(txt)
        
      print_w = f * ln + 2
      
      p(f"Book {idx+1}", "horizontal" if print_w <= w else "vertical")
    
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    
