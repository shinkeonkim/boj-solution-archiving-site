n = int(input())
s = input()

cnt = 1
ans = False
for i in range(1, n):
  if abs(ord(s[i]) - ord(s[i-1])) == 1:
    cnt += 1
  else:
    cnt = 1
  
  if cnt == 5:
    ans = True
    break

print("YES" if ans else "NO")
