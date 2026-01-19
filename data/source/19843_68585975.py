D = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
}

t, n = map(int, input().split())

for i in range(n):
    a, b, c, d = input().split()
    a = D[a]
    c = D[c]
    b = int(b)
    d = int(d)

    t -= c * 24 + d - (a * 24 + b)

if t > 48:
    print(-1)
else:
    print(max(0, t))