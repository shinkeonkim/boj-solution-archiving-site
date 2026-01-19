s=0
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        s+=i
print(s)