def f(a):
    if(a<0):
        return -(a*(a-1)//2)
    else:
        return a*(a+1)//2
for i in range(int(input())):
    a,b=map(int,input().split())
    S1=0
    S2=0
    print("Scenario #",end="")
    print(i+1,end=":\n")
    if(a>0):
        print(f(b)-f(a)+a)
    elif(a<=0 and b>0):
        print(f(b)+f(a))
    else:
        print(f(a)-f(b)+b)
    print()