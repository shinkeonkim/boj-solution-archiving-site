a=input()
a=int(a)
for y in range(0,a):
    for x1 in range(0,y+1):
        print("*",end="")
    for x2 in range(0,(a-y-1)*2):
        print(" ",end="")
    for x1 in range(0,y+1):
        print("*",end="")
    print("")
for y in range(a-1,0,-1):
    for x1 in range(0,y):
        print("*",end="")
    for x2 in range(0,(a-y)*2):
        print(" ",end="")
    for x1 in range(0,y):
        print("*",end="")
    print("")