import hashlib
a=input()
L=hashlib.sha256(a.encode())
print(L.hexdigest())