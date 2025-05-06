def reverse(c):
    x=[]
    for i in c:
        x.append(i)
    i=0
    j=len(c)-1
    while(i<j):
        temp=x[i]
        x[i]=x[j]
        x[j]=temp
        i=i+1
        j=j-1
    c=''
    for i in x:
        c=c+i
    return c        

a=input("enter  a string")
b=""
x=[]
for i in a:
    if i != ' ':
        b=b+i
    else:
        x.append(b)
        b=''
x.append(b)

a=''
for i in x:
    a=a+reverse(i)
    a=a+" "
print(a)    