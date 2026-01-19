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


def solve():
  s = int(input()) - 1
  
  ans = []
  while 1:
    ans.append(s + 1)
    command = input()
    
    if command == '#':
      break
    
    direction = command[0]
    crt_cnt = int(command[1:])
    
    if direction == "C":
      s = (s + crt_cnt) % 8
    else:
      s = (s - crt_cnt + 8) % 8
  
  print(*ans, end = "")
  
  if len(ans) < 5 or len(ans) != len(set(ans)):
     p(" reject")
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
