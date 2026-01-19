n, k = map(int, input().split())

if n == 0:
    print(0)
else:
    ans = 0
    k2 = k
    while k2 <= n:
        ans += n // k2
        k2 *= k
    print(ans)
