import sys
input = sys.stdin.readline

while 1:
  n = int(input())
  if n == 0:
    break
  
  l = sorted([*map(int, input().split())])
  
  
  crt = l[0]
  cnt = 1
  ans = 1
  
  for i in range(1, n):
    if l[i] - 1 == crt:
      cnt += 1
      ans = max(ans, cnt)
    else:
      cnt = 1
    crt = l[i]
  print(ans)