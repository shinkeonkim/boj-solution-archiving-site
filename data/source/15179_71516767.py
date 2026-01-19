import sys
from math import sqrt, pi, sin, factorial
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = " " : [*map(int,inp().split(x))]
mfi = lambda x = " " : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print


def solve():
  names = [input(), input()]
  score = [0, 0]
  
  n = int(input())
  s = input()
  
  for i in range(n):
    if max(score) >= 7:
      break

    if s[i] == 'S':
      continue
    
    if s[i] == 'H':
      score[i % 2] += 1
      
    if s[i] == 'D':
      score[i % 2] += 2
      score[i % 2] = min(7, score[i % 2])
    
    if s[i] == 'O':
      score[1 - i % 2] += 1
  print(f"{names[0]} {score[0]} {names[1]} {score[1]}. ", end="")
  
  if max(score) == 7:
    print(f"{names[score.index(7)]} has won.")
  elif score[0] > score[1]:
    print(f"{names[0]} is winning.")
  elif score[1] > score[0]:
    print(f"{names[1]} is winning.")
  else:
    print("All square.")
  
  
if __name__ == "__main__":
  tc = 1
  
  for t in range(1, tc+1):
    d = solve()
