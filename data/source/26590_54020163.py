a, b = input().split()

k = min(len(a), len(b))
ans=""

for i in range(k):
    ans += (b[i] if i % 2 else a[i])
print(ans)