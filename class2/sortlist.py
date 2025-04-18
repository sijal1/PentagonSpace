a=[]
n=int(input('enter the number of elements : '))
print("enter the elements : ")
a=[int(input()) for i in range(n)]

for j in range(n):
    for i in range(0,(n-2)+1,1):
        if a[i]<a[i+1]:
            a[i]=a[i]+a[i+1]
            a[i+1]=a[i]-a[i+1]
            a[i]=a[i]-a[i+1]
        #print(a)            
print(a)


""" for i in range(n):
    for j in range(n-1):
        if a[j]>a[j+1]:

            a[j],a[j+1]=a[j+1],a[j]
            
        
print(a) """
