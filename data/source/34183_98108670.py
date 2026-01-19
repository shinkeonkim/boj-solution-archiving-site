N, M, A, B = map(int, input().split())

need = max(0, 3 * N - M)

if need > 0:
    print(A * need + B)
else:
    print(0)
