n = int(input())
l = [*map(int, input().split())]

crt = 1

for i in range(n):
    crt *= 2
    crt -= l[i]
        
    if crt < 0:
        print("error")
        break
else:
    crt %= 1000000007
    print(crt)