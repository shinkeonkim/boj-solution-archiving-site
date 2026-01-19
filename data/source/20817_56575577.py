s = input()
ans = s[:2]

for i in range(2, len(s)):
  if ans[-2] == ans[-1] == s[i] and s[i] in "bcdfghjklmnpqrstvwxz":
    continue
  ans += s[i]
print(ans)