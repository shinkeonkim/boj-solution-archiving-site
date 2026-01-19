import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  room, cond = mii()
  mode = inp()
  
  if mode == 'freeze':
    if room > cond:
      room = cond
  elif mode == 'heat':
    if room < cond:
      room = cond    
  elif mode =='auto':
    room = cond
  
  p(room)
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(tc):
    solve()
    