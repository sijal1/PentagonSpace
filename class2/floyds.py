n=4
a=1
#for i in range(1,n+1,1):
#    for j in range(1,i + 1 , 1):
#        print(a," ",end="")
#        a+=1
#    print("")    

for i in range(1,n+1,1):
    for j in range(1,n-i+1,1):      
        print( "  ",end="")
    for j in range(1,i+1,1):
        print( a," ",end="")
        a+=1    
    print("")      