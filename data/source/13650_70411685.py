import sys
inp = lambda : sys.stdin.readline()[:-1]
mii = lambda : [*map(int,input().split())]
ii = lambda : int(input())

while 1:
  try:
    n = ii()
    ans = 0
    A = {}
    B = {}
    for i in range(n):
      a, b = input().split()
      a = int(a)
      
      if b == 'D':
        A[a] = A.get(a, 0) + 1
      else:
        B[a] = B.get(a, 0) + 1
    
    for i in A:
      ans += min(A[i], B.get(i, 0))
    print(ans)
      
  except:
    break