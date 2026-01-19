n = int(input())

l = [[*map(int, input().split())] for i in range(n)]
chk = [False] * n
l.sort(key=lambda t : t[0])

crt = -100000
ans = 0

for x, l in l:
    if x > crt:
        ans += 1
    crt = x + l
print(ans)