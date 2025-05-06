x=[]
a=input("enter a string")
for i in a:
    x.append(i)
print(x)    
print(a)
a=''
for i in x[ : : -1]:
    a=a+i
print(a)    