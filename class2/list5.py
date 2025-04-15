#armstrong nums in list
def length(n):
    l=0
    while(n!=0):
        n=n//10
        l+=1
    return l

def calculate(n,l):
    sum=0
    while(n!=0):
        r=n%10
        sum=sum+(r**l)
        n=n//10
    return sum

n=int(input("enter n : "))
a=[]
print("enter the numbers : ")
a=[int(input()) for i in range(n)]                                                             
print("armstrong numbers ")

for i in a :
    l=length(i)
    if(i == calculate(i,l)):
        print(i)    
    
