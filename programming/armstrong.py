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

n = int(input("enter num : "))
l=length(n)
x=calculate(n,l)

print(x)
if(x==n):
    print("it is an armstrong num")
else:
    print("not an armstrong num")    
