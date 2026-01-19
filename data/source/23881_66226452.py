n, k = map(int, input().split())
l = [*map(int, input().split())]

cnt = 0

for i in range(n):
    idx = 0
    for j in range(0, n-i):
        if(l[j] > l[idx]):
            idx = j

    if idx == n - i - 1:
        continue

    l[idx], l[n - i - 1] = l[n - i - 1], l[idx]
    cnt += 1

    if k == cnt:
        print(l[idx], l[n - i - 1])
        break
else:
    print(-1)