x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)

s=input("enter the character to remove : ")

"""for i in x:
     if i == s :
          x.remove(i) """

a=''
for i in x:
    if i!=s: 
        a=a+i                   
print(a)
