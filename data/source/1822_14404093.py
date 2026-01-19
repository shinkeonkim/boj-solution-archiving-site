n,m=list(map(int,input().split()))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
s=a-b
print(len(s))
s=list(s)
s.sort()
for i in s:
    print(i,end=" ")