s=str(input("Dati un sir de caractere: "))
n=0
for i in s:
    if ((ord(i) in range (32,48)) or (ord(i) in range(58,65)) or (ord(i) in range (91,9)) or (ord(i) in range (123,127))):
        n+=1
print(n)