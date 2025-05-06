def palindrome(c):
    x=[]
    for i in c:
        x.append(i)
    mark=0
    i=0
    j=len(c)-1
    while(i<j):
        if x[i]!=x[j]:
            mark=1
        i+=1
        j-=1     
    if mark==0:
       print(c)     

a=input("enter  a string : ")
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
    palindrome(i)   