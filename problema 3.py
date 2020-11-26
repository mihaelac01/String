x=input("introdu primul cuvant:")
y=input("introdu al doilea cuvant:")
z=input("introdu al treilea cuvant:")
m=input("introdu al patrulea cuvant:")
if ((len(x)<3) or (len(y)<3) or (len(z)<3) or (len(m)<3)):
    print("error")
l1=x[:2]
l2=y[0]
l3=z[:3]
l4=m[:(len(m)//2)]
print("cuvintele:",x,y,z,m,sep=" ")
print("cuvintul format",l1+l2+l3+l4)
