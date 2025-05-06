x=[]
a=input("enter a string: ")

for i in a:
     x.append(i)
mark=0
i=0
j=len(x)-1
while(i<j):
     if x[i]!=x[j]:
          mark=1
     i+=1
     j-=1     
if mark==0:
     print("palindrome")
else:
    print("not palindrome")     



""" b=''
for i in x:
    b=i+b         

if a==b:
    print("palindorme]")
else:
    print("not palinomrme") """