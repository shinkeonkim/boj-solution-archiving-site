for i in range(1,int(input())+1):
    N=int(input())
    for j in range(1, int(input())+1):
        a,b=map(int,input().split())
        N+=a*b
    print(N)