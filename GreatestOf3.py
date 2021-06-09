a=int(input("Enter Number1: "))
b=int(input("Enter Number2: "))
c=int(input("Enter Number3: "))

if(a>b and a>c):
    print(a,"is Greatest")
elif(b>a and b>c):
    print(b,"is Greatest")
elif(c>a and c>b):
    print(c,"is Greatest")
else:
    print(a,",",b,",",c,"are Equal")
