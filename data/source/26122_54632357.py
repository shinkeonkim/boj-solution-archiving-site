n = int(input())
s = input()
l = []

crt = s[0]
cnt = 1

for i in range(1, n):
  if s[i] == crt:
    cnt += 1
  else:
    l.append([crt, cnt])
    crt = s[i]
    cnt = 1
l.append([crt, cnt])

mx = 0
for i in range(1, len(l)):
  if l[i][0] != l[i - 1][0]:
    mx = max(mx, min(l[i][1], l[i - 1][1]) * 2)
print(mx)
