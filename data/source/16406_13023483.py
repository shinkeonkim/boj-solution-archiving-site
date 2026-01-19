n=int(input())
a=input()
b=input()
C=0
for i,j in enumerate(a):
    if(j==b[i]):
        C+=1
print( min(C,n)+min(len(a)-C,len(a)-n))