import hashlib
a=input()
L=hashlib.sha512(a.encode())
print(L.hexdigest())