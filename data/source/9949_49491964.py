tc = 0
while 1:
  tc += 1

  a, b = input().split()

  if a == b == '#':
    break

  print(f'Case {tc}')
  r = '_'
  for i in range(int(input())):
    print(input().replace(a.lower(), r).replace(b.lower(), r).replace(a.upper(), r).replace(b.upper(), r))
  print()
