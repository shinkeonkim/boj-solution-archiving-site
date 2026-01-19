import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s, k):
  ret = ""

  for i in s:
    ret += chr((ord(i) - 97 - k + 26) % 26 + 97)

  if "i" in ret:
    return 0
  return 1

def solve():
  s = input()
  ans = 0
  for i in range(26):
    ans += f(s, i)

  if ans == 0:
    return "impossible"
  return ans

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
    p(ret)