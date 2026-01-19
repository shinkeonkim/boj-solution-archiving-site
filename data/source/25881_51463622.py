n, m = map(int, input().split())
for i in range(int(input())):
    k = int(input())
    s = min(1000, k) * n + max(0, k - 1000) * m
    print(k, s)

    