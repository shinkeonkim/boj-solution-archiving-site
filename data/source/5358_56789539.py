while 1:
    try:
        s = input()
    except:
        break
    print(s.replace("e", "0").replace("E","1").replace("i", "e").replace("I", "E").replace("0", "i").replace("1","I"))
    
    