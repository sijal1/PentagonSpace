n=4
for i in range(1,n+1-1,1):
    for j in range(1,n-i+1,1):
        print(" ",end="")
    for j in range(1,n+1,1):
        if( i== 1 or i==4 or j== 1 or j==4):
            print( "*",end="")
        else:
            print(" ",end="")    
            
    print("")    

