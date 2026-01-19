for i in range(int(input())):
    a,b,c=map(int,input().split())
    if a+b+c==180:
        print(a,b,c,"Seems OK")
    else:
        print(a,b,c,"Check")