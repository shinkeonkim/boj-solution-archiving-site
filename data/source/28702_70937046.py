import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def f(k):
  if k % 3 == k % 5 == 0:
    return "FizzBuzz"
  if k % 3 == 0:
    return "Fizz"
  if k % 5 == 0:
    return "Buzz"
  return k

def solve():
  l = [input() for _ in range(3)]
  
  idx = -1
  
  for i in range(3):
    if 'Fizz' not in l[i] and 'Buzz' not in l[i]:
      idx = i
  
  ans = int(l[idx])+ 3 - idx
  print(f(ans))
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    solve()
