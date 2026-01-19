input()
s = input()

ans = 0
crt = 0

for i in s:
  if i == '1':
    crt = 2
    ans += 1
  else:
    if crt > 0:
      ans += 1
      crt -= 1

print(ans)
