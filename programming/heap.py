pos = [0 for i in range(20)]
neg = [0 for i in range(20)]
print(pos)
print(neg)
n=int(input('enter the number of elements : '))
print("enter the elements : ")
for i in range(n):
    x=int(input())
    if x>0:
        pos[x]=pos[x]+1
    else:
        x=x*-1
        neg[x]=neg[x]+1    
print(pos)
print(neg)
x=int(input("enter the searc element : "))
if x>=0:
    print("occurence = ", pos[x] )
else:
    x=x*-1
    print("occurence = ", neg[x] )    

for i in range(20):
    if neg[i]!=0:
        print(-1*i,end=" ")    
for i in range(20):
    if pos[i]!=0:
        print(i,end=" ")   

#to reverse yhe order:  for i in range(20,0,-1):            