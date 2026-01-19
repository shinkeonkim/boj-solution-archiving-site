n = int(input())
l = [*map(int, input().split())]

mx = 0
for i in range(n):
    mx = max(l[i] - n + i, mx)

print(mx)