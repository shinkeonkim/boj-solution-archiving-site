S,K = map(int,input().split())
L = [0]*K
for i in range(K):
    L[i] += S//K
for i in range(S%K):
    L[i] +=1

ret =1
for i in range(K):
    ret*=L[i]
print(ret)