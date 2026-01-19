def f(h1,m1,t1,h2,m2,t2):
    A=3600*(h2-h1)+60*(m2-m1)+t2-t1
    H=A//3600
    A%=3600
    M=A//60
    T=A%60
    print(H,M,T)
for i in range(3):
    h1,m1,t1,h2,m2,t2=map(int,input().split())
    f(h1,m1,t1,h2,m2,t2)