n = int(input())
l = [input() for i in range(n)]

for i in range(int(input())):
  k = int(input())

  if k > n or k <= 0:
    print(f"Rule {k}: No such rule")
  else:
    print(f"Rule {k}: {l[k - 1]}")