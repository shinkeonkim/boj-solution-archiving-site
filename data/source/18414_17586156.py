X,L,R=map(int,input().split())
ans = R
for i in range(L,R):
    if(abs(i-X) < abs(ans-X)):
        ans = i
print(ans)
