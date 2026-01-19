J, R = map(int, input().split())
l = [*map(int, input().split())]
mx = 0
ans = 0

for i in range(J):
  crt = 0
  for j in range(R):
    crt += l[i + j * J]
  if mx <= crt:
    mx = crt
    ans = i + 1
print(ans)