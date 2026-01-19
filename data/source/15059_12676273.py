L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
S=0
for i in range(3):
   S+= L2[i]-L1[i] if L2[i]>L1[i] else 0
print(S) 