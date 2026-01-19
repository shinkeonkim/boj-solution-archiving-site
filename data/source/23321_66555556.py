l = [input() for i in range(5)]
n = len(l[0])
d = []

for i in range(n):
    s = ""
    for j in range(0, 5):
        s += l[j][i]

    d.append(s)

nxt = { ".omln": "owln.", "owln.": ".omln", "..oLn":"..oLn"}

d2 = []

for i in d:
    d2.append(nxt[i])

for j in range(0, 5):
    for i in range(n):
        print(d2[i][j],end="")
    print()