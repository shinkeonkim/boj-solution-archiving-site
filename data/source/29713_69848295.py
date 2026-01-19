input()
s = input()

x = min([s.count(i) for i in "BONZSILV"])
y = min([s.count(i) for i in "RE"])

print(min(x, y // 2))
