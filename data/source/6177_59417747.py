n = int(input())
l = sorted([int(input()) for i in range(n)])

print(f"{sum(l) / n:.5f}")

if len(l) % 2:
    print(f"{l[n // 2]:.5f}")
else:
    d = (l[n // 2] + l[n // 2 - 1]) / 2
    print(f"{d:.5f}")