import math as m
H,V=map(float,input().split())
a= H*V/(H+m.sqrt(H**2+V**2))
row=m.sqrt(H**2+a**2)/2
S=H*(V-a)
column=S/2/row
print("%.2f %.2f" %(row,column))