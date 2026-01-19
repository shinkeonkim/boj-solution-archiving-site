n = int(input())
l = sorted([int(input()) for i in range(n)])

for i in range(n - 1, 1, -1):
    if l[i] < l[i - 1] + l[i - 2]:
        print(l[i] + l[i-1] + l[i-2])
        break
else:
    print(-1)