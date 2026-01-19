mx = 0
crt = 0
input()
for i in [*map(int, input().split())]:
  if i == 1:
    crt += 1
  else:
    crt = 0
  mx = max(mx, crt)
print(mx)