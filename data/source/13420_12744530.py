for i in range(int(input())):
    L=list(input().split())
    L[0]=int(L[0])
    L[2]=int(L[2])
    L[4]=int(L[4])
    c=False
    if(L[1]=='+'):
        if(L[0]+L[2]==L[4]):
            c=True
    if(L[1]=='-'):
        if(L[0]-L[2]==L[4]):
            c=True
    if(L[1]=='*'):
        if(L[0]*L[2]==L[4]):
            c=True
    if(L[1]=='/'):
        if(L[0]//L[2]==L[4]):
            c=True
    if(c):
        print("correct")
    else:
        print("wrong answer") 