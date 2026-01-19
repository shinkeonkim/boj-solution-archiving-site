k,n=map(int,input().split())
print(n*k//(n-1) + int(((n*k) % (n-1) > 0)) if n > 1 else -1)
