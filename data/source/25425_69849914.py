N, M, a, K = map(int, input().split())

B = a - K

print(min(N, B + 1), B // M + (1 if B%M else 0) + 1)