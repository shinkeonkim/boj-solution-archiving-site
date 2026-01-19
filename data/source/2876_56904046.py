n = int(input())
D = [0] * 6
ans = 0
mx = 0
for i in range(n):
  a, b = map(int, input().split())
  
  for j in range(1, 6):
    if j == a or j == b:
      D[j] += 1
    else:
      D[j] = 0

  for j in range(1, 6):
    if mx < D[j]:
      ans = j
      mx = D[j]
    elif mx == D[j]:
      if ans > j:
        ans = j
print(mx, ans)
