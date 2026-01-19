a, b = map(int, input().split())
c, d = map(int, input().split())

ans = 11111111111111111111111111

for k1 in range(0, 1100):
    for k2 in range(0, 1100):
        if (d - c) + d * k2 == (b - a) +  b * k1:
            ans = min(ans, (d - c) + d * k2)

print(ans)
