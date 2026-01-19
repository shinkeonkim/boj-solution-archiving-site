for _ in range(int(input())):
  input()
  k = len(set([*map(int, input().split())]))
  print((k-1)*2+1)
