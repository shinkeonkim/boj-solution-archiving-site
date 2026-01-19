n, m = map(int, input().split())

l = [*map(int, input().split())]

s = max(l)
e = 100000000000
ans = 2 * e

while s <= e:
    mid = (s + e) // 2
    
    cnt = 1
    crt = l[0]
    
    for i in l[1:]:
        if crt + i <= mid:
            crt += i
        else:
            crt = i
            cnt += 1

    if cnt > m:
        s = mid + 1
    else:
        ans = min(ans, mid)
        e = mid - 1

print(ans)
