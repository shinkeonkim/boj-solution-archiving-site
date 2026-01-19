n=int(input())
for i in range(0,n):
    L=list(map(int,input().split(" ")))
    L.sort()
    print("Scenario #{}:".format(i+1))
    if(L[2]**2==L[0]**2+L[1]**2):
        print("yes\n")
    else:
        print("no\n")
