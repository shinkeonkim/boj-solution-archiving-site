def f():
	n, m = map(int, input().split())
	a = sum([*map(int, input().split())])
	b = sum([*map(int, input().split())])
	
	if n <= m:
		return "Yes"
	return "No"
	
	
for _ in range(int(input())):
	print(f())