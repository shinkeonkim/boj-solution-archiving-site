n = int(input())
l = sorted([[int(input()), i, 0] for i in range(n)], key=lambda t : (-t[0], t[1]))

d = 1
l[0][2] = d

for i in range(1, n):
    if l[i][0] == l[i - 1][0]:
        l[i][2] = d
    else:
        d = i + 1
        l[i][2] = d

l.sort(key=lambda t : t[1])

for _, _, i in l:
    print(i)