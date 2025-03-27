n=4
a=1
for i in range(1,n+1,1):
    for j in range(1,n+1-i+1,1):  
            print( a," ",end="") 
    print("")   
    a+=1
