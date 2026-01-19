d = [0]
s = [0]

cnt = 0
crt = 1
for i in range(10001):
    if crt == cnt:
        crt += 1
        cnt = 0
    d.append(crt)
    s.append(s[-1] + crt)
    cnt += 1

while 1:
    n = int(input())

    if n == 0:
        break

    print(n, s[n])