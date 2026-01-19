D = [0] * 110000
D[1] = 1
D[2] = 2

def f(n):
    if D[n]:
        return D[n]
    
    nxt = n * 3 + 1 if n % 2 else n // 2
    D[n] = max(n, f(nxt))
    
    return D[n]


while 1:
    n = int(input())
    
    if n == 0:
        break
    
    print(f(n))
