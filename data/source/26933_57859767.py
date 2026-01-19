ans = 0
for i in range(int(input())):
    a, b, c = map(int,input().split())
    ans += max(b - a, 0) * c
print(ans)