n, m, q = map(int, input().split())

l = [[*map(int, input().split())] for i in range(n)]

d = [i for i in range(0, n)]

for _ in range(q):
    command = [*map(int, input().split())]
    if command[0] == 0:
        l[d[command[1]]][command[2]] = command[3]
    else:
        d[command[1]], d[command[2]] = d[command[2]], d[command[1]]

for i in range(n):
    print(*l[d[i]])
