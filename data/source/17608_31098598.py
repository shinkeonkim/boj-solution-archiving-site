import sys
n = int(sys.stdin.readline())
L = [int(sys.stdin.readline()) for i in range(n)]

stk = []

for i in range(0, n):
  crt = L[i]
  if len(stk) == 0: # stack이 비어있다면,
    stk.append(L[i]) # stack에 그래도 값을 push한다.
  else:
    while len(stk) > 0 and stk[-1] <= crt:
      stk.pop()
    stk.append(crt)

print(len(stk))