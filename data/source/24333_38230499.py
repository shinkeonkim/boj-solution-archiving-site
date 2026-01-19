a,b,c,d,e=map(int,input().split())
a=max(a,c)
b=min(b,d)
print(max(b-a + 1 - int(a<=e<=b), 0))