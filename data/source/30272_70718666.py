import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())

def f(l):
  l = [i.strip() for i in l]
  if l[0] == "..#####..":
    return 0
  
  if l[0] == "....##...":
    return 1
  
  if l[4] == "##.......":
    return 2
  
  if l[4] == "#########":
    return 4
  
  if l[5] == ".##....##":
    return 5
  
  if l[3] == "########.":
    return 6
  
  if l[4] == "...##....":
    return 7
  
  if l[2] == ".......##":
    return 3
  
  if l[4] == ".......##":
    return 9
  
  return 8
  
  

def solve():
  l =[inp() for _ in range(8)]
  print(f(l), end="")
  

if __name__ == "__main__":
  tc = ii()
  for t in range(tc):
    solve()
    