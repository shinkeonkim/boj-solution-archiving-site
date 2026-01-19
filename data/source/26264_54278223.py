input()
s = input()
b = s.count('b')
y = s.count('y')

if b > y:
  print('bigdata?')
elif b < y:
  print('security!')
else:
  print('bigdata? security!')