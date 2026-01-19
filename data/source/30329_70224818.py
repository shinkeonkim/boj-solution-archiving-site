import sys

input = sys.stdin.readline

s = input()
ans = 0
for i in range(0, len(s) - 4):
  if s[i:i+4] == "kick":
    ans += 1
print(ans)