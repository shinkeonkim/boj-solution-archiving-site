import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  key = input()
  s = input()

  ans = ""

  for i in s:
    if "A" <= i <= "Z":
      k = ord(i) - 65
      ans += key[k].upper()
    elif "a" <= i <= "z":  
      k = ord(i) - 97
      ans += key[k]
    else:
      ans += i
  return ans

if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()

    if ret == None:
      break

    p(ret)