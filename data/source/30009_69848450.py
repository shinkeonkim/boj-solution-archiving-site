N = int(input())
X, Y, R = map(int, input().split())

a = b = 0

for i in range(N):
  K = int(input())
  
  if X - R == K or X + R == K:
    b += 1
  elif X - R < K < X + R:
    a += 1
print(a, b)

