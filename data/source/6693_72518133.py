import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print
  
  
def f(s):
  k = 0
  d = ""  
  for i in range(len(s)):
    if '0' <= s[i] <= '9':
      k *= 10
      k += int(s[i])
    else:
      d = s[i:]
      break
  return (k, d)
    

def solve():
  k = 1 / sqrt(2)
  d = {
    "N": (0, 1),
    "NE": (k, k),
    "E": (1, 0),
    "SE": (k, -k),
    "S": (0, -1),
    "SW": (-k, -k),
    "W": (-1, 0),
    "NW": (-k, k),
  }
  
  while 1:
    s = input()
    
    if s =="END":
      break
    
    s = s[:-1]
    
    l = s.split(",")
    
    crt = [0, 0]
    for direction in l:
      v, _direction = f(direction)
      diff = d[_direction]
      crt[0] += v * diff[0]
      crt[1] += v * diff[1]
    
    step = sqrt(crt[0] ** 2 + crt[1] ** 2)
    p(f"You can go to ({crt[0]:.3f},{crt[1]:.3f}), the distance is {step:.3f} steps.")
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   