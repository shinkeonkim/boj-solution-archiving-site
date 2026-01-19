while True:
    a=int(input())
    if a == -1:
        break
    s,k=0,0
    for i in range(a):
        b,c=map(int,input().split())
        s+=b*(c-k)
        k=c
    print(s,"miles")