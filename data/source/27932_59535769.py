from sys import exit

n, k = map(int, input().split())

if n == k:
    print(0)
    exit()

l = [*map(int, input().split())]
l = [l[0]] + l + [l[-1]]

diff = []
k = n - k

for i in range(1, n+1):
    diff.append(max(abs(l[i] - l[i-1]), abs(l[i] - l[i + 1])))

diff.sort()

i = 0

while i < len(diff):
    if i + 1 < len(diff) and diff[i] == diff[i + 1]:
        i += 1
        continue
    
    if i + 1 >= k:
        print(diff[i])
        break
    
    i += 1