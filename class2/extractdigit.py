
sum=0
n= int(input("enter vakue of n: "))
while(n!=0):
    r=n%10
    n=n//10
    sum=sum+r
print(sum)