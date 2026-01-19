import sys
from math import sqrt, pi, sin, factorial, ceil, floor

BLANK = " "

inp = input
# inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

key = [2] * 3 + [3] * 3 + [4] * 3 + [5] * 3 + [6] * 3 + [7] * 4 + [8] * 3 + [9] * 4
count = [1,2,3] * 5 + [1, 2, 3, 4] + [1, 2, 3] + [1, 2, 3, 4]

def f(s):
  ret = []
  for i in s:
    idx = ord(i) - 97
    
    if len(ret) > 0 and ret[-1][0] == str(key[idx]):
      ret[-1] += str(key[idx]) * count[idx]
    else:
      ret.append(str(key[idx]) * count[idx])
  
  return ret


def solve():
  n = ii()
  l = [input().strip() for _ in range(n)]
  
  S = input()
  _S = []
  crt = S[0]
  for i in S[1:]:
    if crt[-1] == i:
      crt += i
    else:
      _S.append(crt)
      crt = i
  _S.append(crt)
  S = _S    
  
  
  cnt = 0

  for i in l:
    crt = f(i)
    if len(S) != len(crt):
      continue
    
    for j in range(len(S)):
      if S[j] not in crt[j]:
        break
    else:
      cnt += 1
  
  p(cnt)
  
if __name__ == "__main__":
  tc = 1

  for t in range(1, tc+1):
    ret = solve()
   