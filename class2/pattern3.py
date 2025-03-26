
n=3
for i in range(1,n+1,1):

    for j in range(1,5+1,1):    
        print( " ",end="")

    for j in range(1,2+1,1):    
        print("+",end="")    

    for j in range(1,5+1,1):    
       print( " ",end="")    
    print("")    
n=5
for i in range(1,5+1 ,1):
    for j in range(1,i-1+1 , 1):
        print(" ",end="")

    for j in range(1,n-i+1 +1 ,1):
        print("*",end="")

    for j in range(1,2+1,1):    
        print("O",end="")      
    
    for j in range(1,n-i+1 +1 ,1):
        print("*",end="")

    print("")       

for i in range(1,3+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end="")
    for j in range(1,i+1+1,1):
        print("*",end="")
        
    print("")      