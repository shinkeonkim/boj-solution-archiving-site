n = int(input())
l = sorted([*map(int, input().split())])

ans = 0
crt = l[0]

for i in range(1, n):
  if l[i - 1] + 1 != l[i]:
    ans += crt
    crt = l[i]

print(ans + crt)
