n = int(input())
l = [*map(int, input().split())]

l2 = [[l[i], i] for i in range(n)]

l2.sort(key=lambda t: t[0])

u, d = map(int, input().split())

ans = [0] * n

for i, idx in l2:
    if i == 1 and u > 0:
        ans[idx] = 'U'
        u -= 1
    elif i == 2 and d > 0:
        ans[idx] = 'D'
        d -= 1
    elif i == 3 and (u > 0 or d > 0):
        if u > 0:
            ans[idx] = 'U'
            u -= 1
        else:
            ans[idx] = 'D'
            d -= 1

if u > 0 or d > 0:
    print("NO")
else:
    print("YES")
    print("".join(ans))

