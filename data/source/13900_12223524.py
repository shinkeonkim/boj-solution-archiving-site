n=input()
L=list(map(int,input().split(" ")))
S=0
ans=0
for i in L:
    S+=i

for i in L:
    ans+=(S-i)*i
    S-=i
print(ans)
