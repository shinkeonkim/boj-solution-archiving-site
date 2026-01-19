n = int(input())
l = [*map(int, input().split())]

s = sum(l)
a = s // n
left = s % n

ans = 0
for i in l:
    if i > a:
        if left > 0:
            ans += i - a - 1
            left -= 1
        else:
            ans += i - a
print(ans)