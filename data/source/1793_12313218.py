D={}
D[0]=1
D[1]=1
D[2]=3
for i in range(2,330):
    D[i]=D[i-1]+2*D[i-2]

while True:
    try:
        n=int(input())
        print(D[n])
    except EOFError:
        break
