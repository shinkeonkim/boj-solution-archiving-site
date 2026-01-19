def f(a):
  try:
    return int(a)
  except:
    return a
l = sorted([[*map(f, input().split())] for i in range(int(input()))], key= lambda t : t[1])

ans = ""
for a, _, b in l:
  ans += a[b - 1].upper()

print(ans)
