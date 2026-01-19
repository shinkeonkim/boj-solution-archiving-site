import base64
a=input().encode('utf-8')
b=str(base64.decodebytes(a))
print(b[2:-1])