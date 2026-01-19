a=int(input())
for i in range(a):
    L=input().split()
    for i in range(2,len(L)):
        print(L[i],end=" ")
    print(L[0],L[1])