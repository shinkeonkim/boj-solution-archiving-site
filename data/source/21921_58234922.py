n, t = map(int, input().split())
l = [*map(int, input().split())]
s = [0] * n

s[0] = l[0]

for i in range(1, n):
    s[i] = s[i - 1] + l[i]

mx = 0
cnt = 0

for i in range(0, n):
    sm = s[i] - (s[i - t] if i - t >= 0 else 0)

    if mx < sm:
        mx = sm
        cnt = 1
    elif mx == sm:
        cnt += 1

if mx == 0:
    print("SAD")
else:
    print(mx, cnt, sep="\n")