for t in range(1,int(input())+1):
    L=list(map(int,input().split()))
    L.sort()
    print("Case #",end="")
    print(t,end=": ")
    if(L[2]>=L[0]+L[1]):
        print("invalid!")
    else:
        if(L[0]==L[1]==L[2]):
            print("equilateral")
        elif(L[0]==L[1] or L[1]==L[2]):
            print("isosceles")
        else:
            print("scalene")