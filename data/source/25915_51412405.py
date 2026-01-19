s = input() + "ILOVEYONSEI"
ans = 0
for i in range(11):
    ans += abs(ord(s[i]) - ord(s[i + 1]))

print(ans)
