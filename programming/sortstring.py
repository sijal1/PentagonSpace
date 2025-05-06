x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)
n=len(x)
for j in range(n):
    for i in range(0,n-1,1):
        if x[i]>x[i+1]:
            c=x[i]
            x[i]=x[i+1]
            x[i+1]=c

a=''
for i in x:
    a=a+i                   
print(a)


