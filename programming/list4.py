#sum of all elem in list
n=int(input("enter n : "))
a=[]
print("enter the numbers : ")
a=[int(input()) for i in range(n)]                                                             
print("")
sum=0
for i in a :
    sum=sum+i
print("sum of all elements in list")    
print(sum)