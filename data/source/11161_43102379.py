for _ in range(int(input())):
  n = int(input())
  ans = 0
  crt = 0
  for i in range(n):
    a,b=map(int,input().split())
    crt += a
    crt -= b
    ans = min(ans, crt)
  
  print(max(0, -ans))
