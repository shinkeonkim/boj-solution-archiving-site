s = input()
n = len(s)

d = 1

for i in range(2, n):
    if i * i > n:
        break
    if n % i == 0:
        d = i

for i in range(0, d):
    for j in range(i, n, d):
        print(s[j],end="")