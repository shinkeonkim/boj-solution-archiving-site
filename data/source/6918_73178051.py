import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from decimal import Decimal
BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = []
  while 1:
    try:
      k = mii()
      l.extend(k)
    except:
      break
  
  assert(len(l) == 5)
  
  pink, green, red, orange, total = l
  cnt = 0
  mn = 111111111111111111
  for i in range(total // pink + 1):
    for j in range(total // green + 1):
      for k in range(total // red + 1):
        for x in range(total // orange + 1):
          val = i * pink + j * green + k * red + x * orange
          
          if val > total:
            break

          if val == total:
            mn = min(mn, sum([i, j, k, x]))
            print(f"# of PINK is {i} # of GREEN is {j} # of RED is {k} # of ORANGE is {x}")
            cnt += 1
  
  p(f"Total combinations is {cnt}.")
  p(f"Minimum number of tickets to print is {mn}.")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
