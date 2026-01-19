s = input()
ans = 0

d = {
  "A+": 4.5,
  "A": 4.0,
  "B+": 3.5,
  "B": 3.0,
  "C+": 2.5,
  "C": 2.0,
  "D+": 1.5,
  "D": 1.0,
  "F": 0.0,
}

cnt = 0
for i in range(len(s)):
    if s[i] == '+':
        continue
    z = s[i]
    
    if i + 1 < len(s) and s[i + 1] == '+':
      z += '+'
    cnt += 1
    ans += d[z]
  
print(ans / cnt)