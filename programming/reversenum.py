n = int(input("Enter value of n: "))
rev = 0
while n != 0:
    r = n % 10 
    n = n // 10      
    rev = rev * 10  
    rev = rev + r    

print(rev)
