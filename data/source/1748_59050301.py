d = 9
d2 = 9
cnt = 1

ans = 0

n = int(input())

while d <= n:
    ans += d2 * cnt
    
    d2 *= 10
    d = d * 10 + 9
    cnt += 1


prev_d = d // 10

ans += (n - prev_d) * cnt

print(ans)