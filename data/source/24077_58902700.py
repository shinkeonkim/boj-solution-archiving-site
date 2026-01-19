n, m = map(int, input().split())

a = [*map(int, input().split())]
b = [*map(int, input().split())]

ans = 0

for i in a:
    for j in b:
        if i <= j:
            ans += 1
print(ans)
