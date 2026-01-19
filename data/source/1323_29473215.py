d = {}
N,K=map(int,input().split())
n = N
cnt = 0
L = 10**len(str(N))
chk = False
while True:
    cnt += 1
    N = N%K
    if N == 0:
        chk = False
        break
    try:
        d[N] += 1
        chk = True
        break
    except:
        d[N] = 1
        N *= L
        N += n

if chk:
    print(-1)
else:
    print(cnt)
