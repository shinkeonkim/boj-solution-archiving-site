for i in range(int(input())):
  a, b, c = map(int, input().split())

  print("Possible" if c in [a+b, a-b, b-a, a*b, a / b, b / a] else "Impossible")
