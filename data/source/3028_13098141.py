L=[1,0,0]
a=input()
for i in a:
    if i == 'A':
        L[0],L[1]=L[1],L[0]
    if i == 'B':
        L[1],L[2]=L[2],L[1]
    if i == 'C':
        L[0],L[2]=L[2],L[0]
for i,k in enumerate(L):
    if k == 1:
        print(i+1)
