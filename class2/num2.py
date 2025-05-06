n=4
a=10
for i in range(1,n+1,1):
    for j in range(1,n+1-i+1,1):  
        print( a," ",end="") 
        a-=1
    print("")   
