n = int(input())
l = [input() for i in range(n)]

m = int(input())

for i in range(m):
    s, e = map(int, input().split())

    for j in range(s - 1, e):
        print(l[j])