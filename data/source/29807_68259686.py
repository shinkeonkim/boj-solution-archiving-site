n = int(input())
l = [*map(int, input().split())] + [0] * (5 - n)

kor = l[0]
mat = l[1]
eng = l[2]
tam = l[3]
sec = l[4]

a = abs(kor - eng) * (508 if kor > eng else 108)
b = abs(mat - tam) * (212 if mat > tam else 305)
c = sec * 707

print((a + b + c) * 4763)