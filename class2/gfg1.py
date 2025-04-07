n=4
a=1
for i in range(1,4+1,1):
    for j in range(1,n-i+1,1):
        print(" ",end="")
    a=i
    for j in range(1,i+1,1):
        print(a,end="")    
        a-=1
    a=2    
    for j in range(1,i-1+1,1):
        print(a,end="")  
        a+=1  
    print("")  