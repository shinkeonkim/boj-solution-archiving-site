for tc in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))
	a = [0] * n
	cnt = 0

	while 1:
		chk = True
		
		for i in range(n):
			if l[i] % 2 == 1:
				l[i] += 1

		for i in range(n):
			if l[i] != l[(i + 1) % n]:
				chk = False
		
		if chk:
			break

		cnt += 1

		for i in range(n):
			a[(i + 1) % n] = l[i] // 2
			l[i] //= 2

		for i in range(n):
			l[i] += a[i]

	print(cnt)