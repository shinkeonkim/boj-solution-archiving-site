d = {
 "Poblano": 1500, "Mirasol": 6000, "Serrano": 15500, "Cayenne": 40000, "Thai": 75000, "Habanero": 125000
}
s=0
for i in range(int(input())):
    s+=d[input()]
print(s)
    