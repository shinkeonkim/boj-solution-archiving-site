n, p, s = map(int, input().split())
for i in range(s):
	k, *l = [*map(int, input().split())]
	
	if p in l:
		print("KEEP")
	else:
		print("REMOVE")