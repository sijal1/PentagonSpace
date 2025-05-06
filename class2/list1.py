def prime(n):
    c=0
    for i in range(1,n+1,1):
        if n%i==0:
            c=c+1
    if c==2:
        print(n)           

n=int(input("enter n : "))
a=[]
print("enter the numbers : ")
a=[int(input()) for i in range(n)]
for i in a :
    prime(i)