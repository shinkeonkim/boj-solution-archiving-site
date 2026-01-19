class Hamming:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        cnt = 0
        for i in range(len(self.a)):
            if a[i] != b[i]:
                cnt+=1
        return "Hamming distance is {}.".format(cnt)

if __name__ == "__main__":
    for i in range(int(input())):
        a=input()
        b=input()
        C= Hamming(a,b)
        print(C)