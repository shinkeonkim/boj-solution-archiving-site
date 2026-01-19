s = input()
n = len(s)
d = n // 2

if n % 2 == 1 or s[d - 1] != '(' or s[d] != ')' or s.count('|') != n - 2:
  print("fix")
else:
  print("correct")