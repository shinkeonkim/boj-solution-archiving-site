from math import factorial
l = [input() for i in range(10)]

d = []

for i in l:
    if i == "1":
        d.append(100)
    elif len(i) == 3:
        d.append(int(i[-1]) * 10)
    else:
        d.append(int(i[-2:]))

d.sort()

ret = 1

for i in d[1:]:
    ret *= i

ret /= factorial(9)

ret /= 10 ** 9

print(ret)
