a=input()
x=[]
for i in a:
    x.append(i)
for i in range(len(a)):
    if(x[i]>='A' and x[i]<='Z'):
        x[i]=chr(ord(x[i])+32)
        continue    
    if(x[i]>='a' and x[i]<='z'):
        x[i]=chr(ord(x[i])-32)
        continue   
a=''
for i in x:
    a=a+i
print(a)            