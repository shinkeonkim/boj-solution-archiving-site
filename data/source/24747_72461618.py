import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def solve():
  s = input()
  l = [input() for _ in range(7)]
  
  for i in range(7):
    if s == l[i]:
      print("WINNER")
      return

    ret = ""
    
    for j in range(5):
      if s[j] == l[i][j]:
        ret += "G"
      elif l[i][j] in s:
        ret += "Y"
      else:
        ret += "X"
    
    if i == 6:
      print("LOSER")
    else:
      print(ret)


if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()