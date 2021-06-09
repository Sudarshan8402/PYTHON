a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
if(a>b):
    n=b
else:
    n=a
for i in range(1,n+1,1):
    if(a%i==0 and b%i==0):
        gcd=i

print("The GCD of",a,"&",b,"is",gcd)


