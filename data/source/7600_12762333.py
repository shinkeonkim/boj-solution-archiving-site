while 1:
    L=input()
    if L=="#":
        break
    Cnt=0
    for j in range(ord('a'),ord('z')+1):
        check=0
        for i in L:
            if(ord(i)==j or ord(i)==j-32):
                check=1

        if check==1:
            Cnt+=1
    print(Cnt)
        

    