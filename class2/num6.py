n = 5
a=1

for i in range(1, n+1, 1):

    for j in range(1, i - 1 + 1 , 1):
        print(" ", end="")   

    for j in range(1, n - i + 1 + 1):
        print("* ", end="")   
    print("")  

n=4

for i in range(1, n+1, 1):

    for j in range(1, n - i + 1  , 1):
        print(" ", end="") 
  
    for j in range(1, i + 1 + 1 , 1):
        print("* ", end="")  

    print("")    