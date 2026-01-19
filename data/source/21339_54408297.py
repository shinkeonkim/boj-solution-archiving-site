n, k = map(int, input().split())
d, s = map(int, input().split())

ans = (n * d - s * k)

print("impossible" if ans > 100 * (n - k) or ans < 0 else ans / (n - k))
