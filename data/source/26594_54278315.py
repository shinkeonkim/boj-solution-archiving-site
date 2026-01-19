s = input()

ans = 1

for i in range(1, len(s)):
  if s[i] != s[0]:
    break
  ans += 1

print(ans)
