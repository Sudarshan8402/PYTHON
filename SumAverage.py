a=int(input("Enter a Number: "))
#sum
sum=0
for i in range(0,a+1,1):
    sum+=i

#avg
avg=sum/a

print("Sum =",sum)
print("Average =",avg)
