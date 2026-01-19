s = input()
ans = ""
i = 0

while i < len(s):
    ans += s[i]

    i += ord(s[i]) - 64

print(ans)
