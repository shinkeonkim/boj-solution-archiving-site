l = [input().split() for i in range(3)]
l.sort(key=lambda t: -int(t[0]))

a = sorted([int(i[1]) % 100 for i in l])

print("%02d%02d%02d" % (a[0], a[1], a[2]))
print(*[i[2][0] for i in l], sep="")