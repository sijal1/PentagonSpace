n = 3

# Upper 
for i in range(1, n + 1):
    for j in range(1, n - i + 1 + 1):
        print(" ", end="")   
    for j in range(1, 2 * i - 1 + 1):
        print("*", end="")   
    print("")     

# Lower
for i in range(n - 1, 0, -1):
    for j in range(1, n - i + 1 + 1):
        print(" ", end="")   
    for j in range(1, 2 * i - 1 + 1):
        print("*", end="")   
    print("")  
