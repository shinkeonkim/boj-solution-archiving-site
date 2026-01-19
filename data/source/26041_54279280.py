l = input().split()
b = input()

ans = 0

for a in l:
  if len(a) <= len(b):
    continue
  if a[:len(b)] == b:
    ans += 1

print(ans)
