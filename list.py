print("This is SUDARSHAN.K's Program")
n=int(input("Enter the number of elements of list: "))
list=[]
print("Enter the value one by one")
for i in range(0,n):
    list.append(int(input()))
    
print(list)

max=list[0]
min=list[0]
for i in list:
    if max<i:
        max=i
    if min>i:
        min=i


print("Maximun value of list :",max)
print("Minimum value of list:",min)
