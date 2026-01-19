n = int(input())
l = sorted([*map(int, input().split())])

s = 0
for i in range(n):
    s += abs(l[(i + 1) % n] - l[i])

print(s)
