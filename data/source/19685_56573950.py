def f(i):
  s = str(i)
  
  return s == s[::-1]

s, e = map(int, input().split())

for i in range(s, e+1):
  print("Palindrome!" if f(i) else i)
