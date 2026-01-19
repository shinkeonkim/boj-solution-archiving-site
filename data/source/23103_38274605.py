s=0
n = int(input())
a,b=map(int,input().split())
for i in range(n-1):
  c,d=map(int,input().split())
  s+=abs(a-c)+abs(b-d)
  a,b=c,d
print(s)
