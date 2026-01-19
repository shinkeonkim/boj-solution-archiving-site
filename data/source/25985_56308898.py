a, b = map(int, input().split())

org_b = (100 * (100 - a) / (100 - b)) * b / 100
c =  a / org_b
print(f"{c:.8f}")
