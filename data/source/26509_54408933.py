for i in range(int(input())):
  a = sorted([*map(int, input().split())])
  b = sorted([*map(int, input().split())])
  
  if a != b or a[0] + a[1] <= a[2] or a[0]**2 + a[1]**2 != a[2] **2:
    print("NO")
    continue

  print("YES")
