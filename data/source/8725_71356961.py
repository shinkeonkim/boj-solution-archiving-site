ans = 0
for i in range(int(input())):
	l = [*map(int,input().split())]
	ans+= max(0, max(l))
print(ans)