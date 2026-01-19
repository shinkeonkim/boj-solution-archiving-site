import sys
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda : [*map(int,input().split())]
ii = lambda : int(input())

crt = (0, 2000)

for i in range(ii()):
  h1, m1, h2, m2 = mii()
  
  s = h1 * 60 + m1
  e = h2 * 60 + m2

  if e <= crt[0] or crt[1] <= s:
    print("NE")
    break
    
  
  crt = (max(crt[0], s), min(crt[1], e))
else:
  print("TAIP")
  print(crt[0] // 60, crt[0] % 60, crt[1] // 60, crt[1] % 60)