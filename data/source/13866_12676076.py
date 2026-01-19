Min=987654321
A,B,C,D=map(int,input().split())
if(abs(A+B-C-D)<Min): Min=abs(A+B-C-D)
if(abs(A+C-B-D)<Min): Min=abs(A+C-B-D)
if(abs(A+D-B-C)<Min): Min=abs(A+D-B-C)
print(Min)