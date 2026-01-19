a=input()
a=int(a)

for i in range(0,a):
    b=input()
    b=list(b)
    b.reverse()
    c=b[:]
    b.reverse()
    A=""
    B=""
    
    for x in b:
        A=A+x
    for y in c:
        B=B+y
    
    A=int(A)
    B=int(B)
    R=A+B
    R=str(R)
    R=list(R)
    R.reverse()
    
    T=R[:]
    R.reverse()
    
    if(R==T):
        print("YES")
    else:
        print("NO")
        
