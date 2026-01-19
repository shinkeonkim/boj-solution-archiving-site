import hashlib
a=input()
L=hashlib.sha384(a.encode())
print(L.hexdigest())