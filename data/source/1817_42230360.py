def solve():
  n, m = map(int,input().split())

  if n == 0:
    print(0)
    return

  l = [*map(int, input().split())]

  ans = c = 0

  for i in l:
    if c - i >=0:
      c -= i
    else:
      c = m - i
      ans += 1

  print(ans)

solve()
