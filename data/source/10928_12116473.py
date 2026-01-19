import hashlib
a=input()
L=hashlib.sha1(a.encode())
print(L.hexdigest())