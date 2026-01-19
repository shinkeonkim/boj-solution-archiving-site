import hashlib
a=input()

L=hashlib.md5(a.encode())

print(L.hexdigest())