n = int(input())

l = [*map(int,input().split())]

m = int(input())

for _ in range(m):
	a,b,c=map(int,input().split())
	b-=1
	c-=1
	
	if a == 1:
		for i in range(b,c+1):
			l[i] = (l[i]*l[i]) % 2010
	else:
		print(sum(l[b:(c+1)]))