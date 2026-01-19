import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  l = [
    "1QAZ",
    "2WSX",
    "3EDC",
    "45RTFGVB",
    "67YUHJNM",
    "8IK,",
    "9OL.",
    "0-=P[];'/",
  ]
  
  cnt = [0] * 8
  
  s = input()
  
  for i in s:
    for j in range(8):
      if i in l[j]:
        cnt[j] += 1
  print(*cnt, sep = "\n")
    
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
