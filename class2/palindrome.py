org = int(input("Enter value of n: "))
n=org
rev = 0
while n != 0:
    r = n % 10 
    n = n // 10      
    rev = rev * 10  
    rev = rev + r    

if(org==rev):
    print("palindrome")
else:
    print("not palidnrome")    