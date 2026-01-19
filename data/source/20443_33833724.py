MOD = 1_000_000_007
derangement = [1, 0, 1, 2, 9]

for i in range(5, 110):
  derangement.append(((i-1) * (derangement[-1] + derangement[-2])) % MOD)

def nCr(n, k):
  ret = 1
  for i in range(n, n-k, -1):
    ret *= i
  for i in range(1, k+1):
    ret //= i
  return ret

n = int(input())
k = n % 4
print((derangement[n - k] * nCr(n, k)) % MOD)
