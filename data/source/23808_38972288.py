n = int(input())
a=("@"*n+" "*n*3+"@"*n+"\n")*n
b=("@"*n*5+"\n")*n
print(a+2*(a+b))
