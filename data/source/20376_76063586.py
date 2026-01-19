import sys

inp = lambda : sys.stdin.readline()
p = print


def solve():
    d = {}
    while 1:
        try:
            s = inp()
        except:
            break
        
        if len(s) == 0:
            break

        crt = s[11:]
        d[crt] = d.get(crt, 0) + 1
    
    p(len(d.values()))

if __name__ == "__main__":
    tc = 1
    for t in range(1, tc+1):
        ret = solve()
