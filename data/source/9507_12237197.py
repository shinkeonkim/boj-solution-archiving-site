L={}

N=input()
N=int(N)

for k in range(0,N):
    a=input()
    a=int(a)

    L[0]=1
    L[1]=1
    L[2]=2
    L[3]=4

    for i in range (4,a+1):
        L[i]=L[i-1]+L[i-2]+L[i-3]+L[i-4]
    print(L[a])