import hashlib
a=input()
L=hashlib.sha224(a.encode())
print(L.hexdigest())