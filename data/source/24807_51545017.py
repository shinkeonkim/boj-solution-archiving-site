a, b, c, d = map(int ,input().split())
chk = False
for i in range(0, d // a + 1):
    for j in range(0, d // b + 1):
        for k in range(0, d // c + 1):
            if a * i + b * j + c * k == d:
                chk = True
                print(i, j, k)

if not chk:
    print("impossible")
