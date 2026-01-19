w1,h1,w2,h2,*z = map(int,open(0).read().split())
print(w1+w2+2*(h1+h2)+abs(w1-w2)+4)
