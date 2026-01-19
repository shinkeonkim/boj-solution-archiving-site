n = int(input())
l = [input() for i in range(n)]

d = -1

for i in range(n):
    if l[i] == '?':
        d = i

s = "#" if d == 0 else l[d - 1][-1]
e = "#" if d == n - 1 else l[d + 1][0]

m = int(input())

for i in range(m):
    a = input()

    if a in l:
        continue

    if (a[0] == s or s == "#") and (a[-1] == e or e == "#"):
        print(a)
        break