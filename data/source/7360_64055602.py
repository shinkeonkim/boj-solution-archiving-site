def f(a, b):
    if a == b:
        return [0, 0]

    if a == 1 and b == 2:
        return [6, 0]
    if a == 2 and b == 1:
        return [0, 6]
    
    s = a + b
    if abs(a - b) == 1:
        return [s, 0] if a < b else [0, s]
    
    m = max(a, b)

    return [m, 0] if a > b else [0, m]


while 1:
    n = int(input())
    
    if n == 0:
        break
    
    a, b = 0, 0
    
    aa = [*map(int, input().split())]
    bb = [*map(int, input().split())]

    for i in range(n):
        c, d = f(aa[i], bb[i])
        a += c
        b += d
    print("A has {} points. B has {} points.\n".format(a, b))