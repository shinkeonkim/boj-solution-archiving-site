n = int(input())

chk = True
ans = 0

for i in range(n):
  if int(input()) * 5 - int(input()) * 3 <= 40:
    chk = False
  else:
    ans += 1

print(ans, ("+" if chk else ""), sep="")
