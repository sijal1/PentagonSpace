#palindromes in list
def reverse(n):
    a=n
    rev=0
    while(n!=0):
        r=n%10
        n=n//10
        rev=rev*10
        rev=rev + r
    if(a==rev):
        print(rev)   
    


n=int(input("enter n : "))
a=[]
print("enter the numbers : ")
a=[int(input()) for i in range(n)]                                                             
print("")
for i in a :
    reverse(i)    
