cnp=input("introdu CNP:")
nr=0
if (len(cnp<13)or(len(cnp)>13)):
    print("nu este corect")
else:
    for n in cnp:
        if ord(n) in range(48,58):
            nr+=1
        if(nr==13):
            print("este corect")
        else:
            print("nu este corect")