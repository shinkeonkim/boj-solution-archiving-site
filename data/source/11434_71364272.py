for tc in range(int(input())):
	print(f"Data Set {tc + 1}:")
	
	n, w, e = map(int, input().split())
	
	ans = 0
	
	for i in range(n):
		l = [*map(int, input().split())]
		
		ans += max(l[0]*w + l[2]*e, l[1]*w + l[3]*e)
	print(ans)
	print()