n, k = map(int, input().split())
s = input()

ans = s[:k-1]
for i in range(k-1, n):
  ans += s[i].lower() if s[i].upper() == s[i] else s[i].upper()

print(ans)
