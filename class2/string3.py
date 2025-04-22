x=[]
a=input("enter a string")
for i in a:
    x.append(i)
i=0
j=len(a)-1
while(i<j):
    c=x[i]
    x[i]=x[j]
    x[j]=c
    i+=1
    j-=1
    print(x)
a=""
for i in x:
    a=a+i    
print(a)    
