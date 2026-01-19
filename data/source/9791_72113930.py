import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(s):
  crt = s[0]
  cnt = 1
  ans = ""
  
  for i in s[1:]:
    if i == crt:
      cnt += 1
    else:
      ans += str(cnt) + crt
      crt = i
      cnt = 1
  
  ans += str(cnt) + crt
  
  return ans


def solve():
  while 1:
    s = input()
    
    if s == "0":
      break
    
    print(f(s))
  
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

