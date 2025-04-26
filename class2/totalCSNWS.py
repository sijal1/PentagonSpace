x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)
     
capital=0
small=0
number=0
special=0
words=0

for i in x:
    if i >= 'A' and i<='Z':
          capital+=1
    elif i >= 'a' and i <= 'z':
          small+=1      
    elif ord(i) >= 48 and ord(i) <=57:
          number+=1              
    elif ord(i) == 32 :
         words+=1      
    else :
           special+=1   
print('total capital : ',capital)
print("total small " , small)
print("total number ",number)
print("total words ",words+1)
print("special charataers ", special)