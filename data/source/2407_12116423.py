Matrix = [[0]*110 for i in range(110)]

def f(N,M):
    global Matrix
    if(Matrix[N][M]):
        return Matrix[N][M]
    elif N==M or M==0:
        return 1
    elif N<M:
        Matrix[N][M]=0
        return Matrix[N][M]
    elif M==1:
        Matrix[N][M]=N
        return Matrix[N][M]
    else:
        Matrix[N][M]=f(N-1,M)+f(N-1,M-1)
        return Matrix[N][M]
n,m=map(int,input().split(" "))
print(f(n,m))