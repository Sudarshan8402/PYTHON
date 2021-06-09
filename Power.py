a=int(input("Enter a Base: "))
b=int(input("Enter th Power: "))
result=1
for i in range(1,b+1):
    result=result*a
print("The value of",a,"to the power",b,"is",result)
