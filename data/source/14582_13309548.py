S1=0
S2=0
check = False

def f():
    global S1,S2,check
    if(S1>S2):
        check=True

A=list(map(int,input().split()))
B=list(map(int,input().split()))
for i in range(0,9):
    S1+=A[i]
    f()
    S2+=B[i]
    f()

if(check):
    print("Yes")
else:
    print("No")
