import sys
from math import sqrt, pi, sin, factorial, ceil, floor
from datetime import datetime, timedelta

BLANK = " "

#inp = input
inp = lambda : sys.stdin.readline()[:-1].strip()
mii = lambda x = BLANK : [*map(int,inp().split(x))]
mfi = lambda x = BLANK : [*map(float,inp().split(x))]
ii = lambda : int(inp())
fi = lambda : float(inp())
p = print

def f(s):
  ret = ""
  
  for i in s:
    if '0' <= i <= '9':
      continue
    ret += i
  return ret

def g(s):
  ret = ""
  
  for i in s:
    if 'a' <= i <= 'z':
      ret += i.upper()
    elif 'A' <= i <= 'Z':
      ret += i.lower()
    else:
      ret += i
  return ret
  

def solve():
  password, inp = input().split()
  
  if password == inp:
    return 0
  
  if len(password) < len(inp):
    return 4

  cap = g(password)
  no_number = f(password)
  two = g(f(password))
  
  if cap == inp:
    return 1
  
  if no_number == inp:
    return 2
  
  if two == inp:
    return 3
  
  return 4
  
if __name__ == "__main__":
  tc = ii()

  for t in range(1, tc+1):
    ret = solve()
    
    messages = [
      "Login successful.",
      "Wrong password. Please, check your caps lock key.",
      "Wrong password. Please, check your num lock key.",
      "Wrong password. Please, check your caps lock and num lock keys.",
      "Wrong password."
    ]
    
    p(f"Case {t}: {messages[ret]}")