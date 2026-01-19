import re
try:
 if re.compile("(100+1+|01)+").fullmatch(input())!=None:
  print("SUBMARINE")
 else:
  print("NOISE")
except:
 print("NOISE")