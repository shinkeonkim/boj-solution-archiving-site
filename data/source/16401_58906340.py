m, n = map(int, input().split())
l = [*map(int, input().split())]

ans = 0
s = 1
e = 10000000000

while s <= e:
    mid = (s + e) // 2
    
    cnt = 0
    
    for i in l:
        cnt += i // mid
        
    if cnt >= m:
        ans = max(ans, mid)
        s = mid + 1
    else:
        e = mid - 1
print(ans)