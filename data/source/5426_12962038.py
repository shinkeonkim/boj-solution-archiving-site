import math
for i in range(int(input())):
    a=input()
    N=int(math.sqrt(len(a)))
    for i in range(N-1,-1,-1):
        for j in range(0,N):
            print(a[i+N*j],end="")
    print()