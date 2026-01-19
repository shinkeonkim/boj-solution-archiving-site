def f(s):
	h,m,s=map(int, s.split(":"))

	return h * 3600 + m* 60 + s

for _ in range(int(input())):
	a, b, c = input().split()
	a = f(a)
	b = f(b)
	c = int(c) * 60
	
	t = b - a if a < b else 86400 - a + b
	
	if c <= t:
		print("Perfect")
	elif c <= t + 3600:
		print("Test")
	else:
		print("Fail")