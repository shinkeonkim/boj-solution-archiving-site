for i in range(0,3):
    S=0
    for x in range(0,int(input())):
        S=S+int(input())
    if(S==0):
        print("0")
    elif(S>0):
        print("+")
    else:
        print("-")
