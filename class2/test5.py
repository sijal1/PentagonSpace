n=int(input("enter num "))
i=1
c=1
while(i!=n):
    if(n%i==0):
        c=c+1
    i=i+1
if c <= 2 :
    print("prime")        
else:
    print("not prime")