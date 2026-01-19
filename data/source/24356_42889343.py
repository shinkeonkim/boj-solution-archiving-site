t1,t2,m1,m2=map(int,input().split())
t = t1*60+t2
m = m1*60+m2
a = m-t

if a < 0:
  a += 1440

print(a, a // 30)