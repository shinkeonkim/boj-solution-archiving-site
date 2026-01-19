n, k = map(int, input().split())
cnt = 0

for i in range(n):
  a = int(input())
  
  while a % 2 == 0:
    cnt += 1
    a //= 2

print(int(cnt >= k))