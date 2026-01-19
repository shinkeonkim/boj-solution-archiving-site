def f(x):
    if x & 1:
        return (x << 1) ^ 6
    else:
        return (x >> 1) ^ 6

x, n = map(int, input().split())

for i in range(n):
    x = f(x)
print(x)
