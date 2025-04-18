a=[]
n=int(input('enter the number of elements : '))
print("enter the elements : ")
a=[int(input()) for i in range(n)]

i=0
j=n-1
while i<j:
    a[i]=a[i]+a[j]
    a[j]=a[i]-a[j]
    a[i]=a[i]-a[j]
    i+=1
    j-=1
print(a)