a=[]
n=int(input('enter the number of elements : '))
print("enter the elements : ")
a=[int(input()) for i in range(n)]
x=int(input('enter the search elemet  : '))
count=0
for i in a:
    if i == x :
        count=count+1
if count==0:
    print("element not found")
else:
    print('element found')
    print("total occurence",count)            
