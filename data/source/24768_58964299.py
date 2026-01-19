while 1:
    a,b=map(int,input().split())
    
    if a == b == 0:
        break
    if a + b == 13:
        ret="Never speak again."
    elif a == b:
        ret="Undecided."
    elif a> b:
        ret="To the convention."
    else:
        ret="Left beehind."
    print(ret)