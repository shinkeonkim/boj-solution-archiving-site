while 1:
	n = int(input())
	
	if n == 0:
		break
	l = [*map(int, input().split())]
	
	ans = 0
	
	for i in range(n):
		p = (i - 1 + n) % n
		q = (i + 1) % n
		
		if l[p] < l[i] > l[q] or l[p] > l[i] < l[q]:
			ans += 1
	print(ans)