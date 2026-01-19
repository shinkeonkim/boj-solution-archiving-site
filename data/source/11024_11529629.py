a=input()
a=int(a)
for i in range(0,a):
    L=list(map(int,input().split(" ")))
    S=0
    for x in L:
        S=S+x
    print(S)