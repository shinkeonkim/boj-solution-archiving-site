def gcd(a, b):
    return gcd(b, a%b) if b > 0 else a 

while True:
    a,b = map(int, input().split())
    if a + b == 0:
        break
    print((a // gcd(a,b)) * (b // gcd(a,b)))
