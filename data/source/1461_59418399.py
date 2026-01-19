n, k = map(int, input().split())

l = [*map(int, input().split())]

plus = []
minus = []

for i in l:
    if i > 0:
        plus.append(i)
    else:
        minus.append(i)

plus.sort(reverse=True)
minus.sort()

distances = []

for i in range(0, len(plus), k):
    distances.append(plus[i])

for j in range(0, len(minus), k):
    distances.append(-minus[j])

distances.sort()

s = 0

for i in distances[:-1]:
    s += i * 2
s += distances[-1]

print(s)
