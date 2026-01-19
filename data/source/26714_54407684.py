n = int(input())
s = input()
k = n // 10
ans = 0

for i in range(0, n, k):
  x = set(list(s[i:i+k]))
  
  if len(x) == 1 and list(x)[0] == 'T':
    ans += 1
print(ans)
