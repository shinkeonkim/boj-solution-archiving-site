for _ in range(int(input())):
  n, *l = [*map(int, input().split())]
  
  d = l[1] - l[0]
  
  chk = True
  for i in range(1, n - 1):
    if d != l[i + 1] - l[i]:
      chk = False
  
  ans = [l[-1] + d * (i + 1) for i in range(5)]
  
  if not chk:
    print(f"The sequence {l} is not an arithmetic sequence.")
  else:
    print(f"The next 5 numbers after {l} are: {ans}")