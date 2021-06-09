a=int(input("Enter a Number: "))
original=a
rev=0
while(a>0):
    unit=a%10
    rev=rev*10+unit
    a=(int)(a/10)
print("Reverse of",original,"is",rev)
