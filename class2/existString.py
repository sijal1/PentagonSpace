x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)
s=input("enter the search elem : ")
count=0
for i in x:
     if i == s :
          count+=1
if count==0:
     print("not found")
else:               
     print("found ",count)        