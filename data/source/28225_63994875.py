n, f = map(int, input().split())
l = [[i, *map(int, input().split())] for i in range(n)]
l.sort(key=lambda t : ((f - t[1]) / t[2]))
print(l[0][0] + 1)