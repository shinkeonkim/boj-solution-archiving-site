p, n = map(int, input().split())
l = sorted([*map(int, input().split())])
idx = 0
while p < 200 and idx < n:
    p += l[idx]
    idx += 1

print(idx)
