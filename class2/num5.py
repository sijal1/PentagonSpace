n=5
a=1
for i in range(1,n+1,1):
    for j in range(1,n+1,1):
        if(i ==1 or j == 1 or i == 5 or j == 5):
            print(a," ",end="")
        elif(i == 2 or j == 2 or i == 4 or j == 4): 
            print(a+1," ",end="")
        if(i ==3 and j == 3):
            print(a+2," ",end="")
    print("")   