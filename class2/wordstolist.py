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
print(x)            