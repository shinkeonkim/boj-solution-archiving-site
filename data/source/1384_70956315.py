import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


# 1384 풀고 있다 끝
def solve():
  tc = 0
  while 1:
    tc += 1
    n = ii()
  
    if n == 0:
      break
      
    l = [input().split() for _ in range(n)]
    
    names = [l[i][0] for i in range(n)]
    
    l = [l[i][1:] for i in range(n)]
    
    ans = []
    for i in range(n):
      for j in range(n - 1):
        if l[i][j] == 'N':
          
          crt = (n + i - 1) % n
          for k in range(j):
            if crt == i:
              crt = (n + crt - 1) % n
            crt = (n + crt - 1) % n
          
          ans.append([names[crt], names[i]])
        
    print(f"Group {tc}")
    
    if len(ans) == 0:
      print("Nobody was nasty")
    else:
      for a, b in ans:
        print(f"{a} was nasty about {b}")
    print()
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
