import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(x):
  l = []
  while x > 0:
    l.append(x % 2)
    x //= 2
  
  while len(l) < 8:
    l.append(0)
  
  return l

def h(l):
  for i in range(8):
    if l[i] > 1:
      if i + 1 < 8:
        l[i + 1] += l[i] // 2
      l[i] = l[i] % 2
  return l

def g(x):
  k = f(x)
  k = [1- i for i in k]
  k[0] += 1
  k = h(k)
  
  return k

def sm(a, b):
  ret = [0] * 8
  for i in range(8):
    ret[i] = a[i] + b[i]
  
  return h(ret)

  
def solve():
  while 1:
    a, b = mii()
  
    if a == b == 0:
      break
    
    p(end=f"{a} = ")
    p(*f(a)[::-1],sep="")
    p(end=f"{b} = ")
    p(*f(b)[::-1],sep="")
          
    p(end=f"-{a} = ")
    p(*g(a)[::-1],sep="")
    p(end=f"-{b} = ")
    p(*g(b)[::-1],sep="")
    p(end=f"{a-b} = ")
    p(*sm(f(a), g(b))[::-1],sep="")
    p()
    
        
if __name__ == "__main__":
  tc = 1
  for t in range(1, tc+1):
    solve()

    