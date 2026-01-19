from sys import stdin

stack = []

n = int(stdin.readline().rstrip())

for i in range(0, n, 1):
  order = stdin.readline().rstrip()
  if 'push' in order:
    order, num = order.split()
    stack.append(int(num))
    # print(*stack)
  elif order == 'pop':
    if len(stack) == 0:
      print(-1)
    else:
      print(stack[-1])
      stack.pop()
  elif order == 'size':
    print(len(stack))
  elif order == 'top':
    if len(stack) == 0:
      print(-1)
    else :
      print(stack[-1])
  elif order == 'empty':
    if len(stack) == 0:
      print(1)
    else:
      print(0)

# print(order)