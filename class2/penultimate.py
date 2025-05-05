a=input("enter  a string: ")
b=""
x=[]
for i in a:
    if i != ' ':
        b=b+i
    else:
        x.append(b)
        b=''

x.append(b)
n=len(x)-2
penu=x[n]
print(penu)            