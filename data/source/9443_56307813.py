l = sorted([ord(input()[0]) for i in range(int(input()))])

ans = 0
crt = 65
i = 0
while i < len(l):
  if l[i] == crt:
    i += 1
    ans += 1
    crt += 1
  elif l[i] < crt:
    i += 1
  else:
    break
print(ans)
