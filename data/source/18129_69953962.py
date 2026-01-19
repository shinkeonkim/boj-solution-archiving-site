ans = ""

s, k = input().split()
s = s.lower()
k = int(k)
d = {}

crt = s[0]
ln = 1

for i in range(1, len(s)):
  if s[i] == crt:
    ln += 1
    continue
  
  is_used = d.get(crt, False)
  
  if not is_used:
    ans += "1" if ln >= k else "0"
    d[crt] = True

  crt = s[i]
  ln = 1

is_used = d.get(crt, False)
if not is_used:
  ans += "1" if ln >= k else "0"

print(ans)