def f(n, s):
  for y in range(n):
    for i in s:
      for x in range(n):
        print(end=i)
    print()

n = int(input())

f(n, "@   @")
f(n, "@  @")
f(n, "@@@")
f(n, "@  @")
f(n, "@   @")
