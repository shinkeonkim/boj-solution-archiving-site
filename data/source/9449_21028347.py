A, B, a, b = map(float,input().split())
cnt1 = 0
cnt2 = 0
while A > 0:
    A -= a
    if A >= 0:
        cnt1+=1
    A -= (a-0.000001)
while B > 0:
    B -= b
    if B >= 0:
        cnt2 +=1
    B -= (b-0.000001)
print(cnt1*cnt2)