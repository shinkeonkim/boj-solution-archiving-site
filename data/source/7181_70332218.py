import sys

# input = sys.stdin.readline

def f(a, b):
  _a = sorted(a)
  _b = sorted(b)

  i = j = ret = 0
  
  while i < 4 and j < 4:
    if _a[i] == _b[j]:
      i += 1
      j += 1
      ret += 1
    elif _a[i] < _b[j]:
      i += 1
    else:
      j += 1
  return ret

def g(a, b):
  ret = 0
  for i in range(4):
    if a[i] == b[i]:
      ret += 1
  return ret

a = list(input())
for i in range(int(input())):
  b = list(input())
  print(f(a, b), g(a, b))