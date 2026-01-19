l = [list(input()) for i in range(int(input()))]

cnt = [0] * 5

for s in l:
    for i in range(5):
        if s[i] == 'Y':
            cnt[i] += 1

mx = max(cnt)

print(*[i + 1 for i in range(5) if cnt[i] == mx], sep=",")