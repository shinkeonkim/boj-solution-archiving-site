a=int(input())
b=int(input())

if(a==2 and b==18):
    print("Special")
elif(a==1 or(a==2 and b<18)):
    print("Before")
else:
    print("After")