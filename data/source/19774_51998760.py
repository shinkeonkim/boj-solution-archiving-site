def f(a):
	a, b = int(a[:2]), int(a[2:])
	ret = (a * a + b * b) % 7
	if ret == 1:
		return "YES"
	return "NO"


for i in range(int(input())):
	print(f(input()))
