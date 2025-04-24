x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)
     
count=0
for i in x:
     if i == " " :
          count+=1

if count==0:
     print(" no words")
else:
     print("total words : ",count+1)           