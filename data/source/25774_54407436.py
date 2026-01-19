d, m, y, n = map(int, input().split())
a = y * 360 + m * 30 + d
d, m, y = map(int, input().split())
b = y * 360 + m * 30 + d
n -= 1

diff = (b - a) % 7
n = (n + diff) % 7 + 1

print(n)
