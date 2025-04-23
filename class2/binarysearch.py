a=[]
n=int(input('enter the number of elements : '))
print("enter the elements : ")
a=[int(input()) for i in range(n)]
x=int(input('enter the search elemet  : '))
count=0
left=0
right=n-1
while(left<=right):

    mid=(left+right)//2
    if(x==a[mid]):
        count+=1
        break
    
    elif x>a[mid]:
        left=mid+1
    
    else:
        right=mid-1

if count==0:
    print("not found")
else:
    print("found")                