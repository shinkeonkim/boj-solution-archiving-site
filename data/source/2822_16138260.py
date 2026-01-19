L = [(int(input()),i)for i in range(8)]
L.sort(key = lambda t:t[0],reverse = True)
print(sum([L[i][0] for i in range(5)]))
K = [L[i][1]+1 for i in range(5)]
K.sort()
for i in K:
    print(i,end=" ")