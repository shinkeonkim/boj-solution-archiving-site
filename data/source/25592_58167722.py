n = int(input())

sm = 0
crt = 1

while sm < n:
    sm += crt
    crt += 1

if crt % 2 == 0:
    print(sm - n)
else:
    if sm == n:
        print(crt)
    else:
        print(0)
