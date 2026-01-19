N = int(input())
l = [*map(int, input().split())]

mn_diff = 999999
ans = (-1, -1)

for i in l:
  if N % i == 0:
    ans = (i, N)
    mn_diff = 0
    break

  a = N - (N % i)
  
  if abs(a - N) < mn_diff:
    mn_diff = abs(a - N)
    ans = (i, a)
  
  a = N + (i - N % i)
  if abs(a - N) < mn_diff:
    mn_diff = abs(a - N)
    ans = (i, a)
    
print(*ans)
