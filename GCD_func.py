#Function
def GCD(a,b):
    if a>b:
        small=b
    else:
        small=a
    for i in range(1,small+1,1):
        if(a%i==0 and b%i==0):
            gcd=i
    return gcd

a=int(input("Enter a Number: "))
b=int(input("Enter a Number: "))
print("The GCD of",a,"&",b,"is",GCD(a,b))
