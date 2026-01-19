input()
s = input()
ans = len(s)
for i in "HIARC":
  ans = min(ans, s.count(i))
print(ans)
