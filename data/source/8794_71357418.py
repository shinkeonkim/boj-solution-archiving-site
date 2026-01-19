for _ in range(int(input())):
	n, m, l = map(int, input().split())
	
	z = n - (m - l + 1) if l !=1 else n
	
	print(z // m + int(z % m > 0))