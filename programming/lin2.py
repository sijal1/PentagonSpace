a=[]
n=int(input('enter the number of elements : '))
print("enter the elements : ")
a=[int(input()) for i in range(n-1)]

sum=0
for i in range(n+1):
    sum=sum+i

sum1=0
for i in a:
    sum1=sum1+i

print("missing num :")
print(sum-sum1)    