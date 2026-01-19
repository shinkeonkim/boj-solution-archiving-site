import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  place_num = {}
  num_place = {}
  
  n = ii()
  l = mii()
  
  m = ii()
  task = mii()
  
  for i in range(n):
    place_num[l[i]] = i + 1
    num_place[i + 1] = l[i]
    
  
  for i in range(m):
    task_num = task[i]
    
    crt_place = num_place[task_num]
    
    if crt_place >= 2019:
      continue
    
    if place_num.get(crt_place + 1, -1) != -1:
      continue
    
    num_place[task_num] = crt_place + 1
    place_num[crt_place + 1] = task_num
    place_num[crt_place] = -1
      
  for i in range(1, n + 1):
    p(num_place[i])
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
