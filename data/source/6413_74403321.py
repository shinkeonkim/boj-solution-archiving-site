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

def num(s):
  k = "A23456789TJQK"
  
  return k.index(s)


def solve():
  while 1:
    l = [[] for _ in range(13)]

    cards = []
    
    for _ in range(4):
      c = input()
      if c == '#':
        return
      cards.extend(c.split())
  
    cards.reverse()
    for i in range(52):
      l[i % 13].append(cards[i])

    cnt = 0
    last = ""
    cur = 12
    for _ in range(52):
      if len(l[cur]) == 0:
        break
      cnt += 1
      last = l[cur][-1]    
      l[cur].pop()

      nm = num(last[0])

      if len(l[nm]) == 0:
        break

      l[cur].append(l[nm][-1])
      l[nm].pop()


    p(f"{cnt:02d},{last}")
  
  
    
    
tc = 1

for t in range(1, tc+1):
  ret = solve()
  
