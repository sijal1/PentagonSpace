x=[]
a=input("enter a string: ")
for i in a:
     x.append(i)

pos = [0 for i in range(150)]

n=len(a)
for i in range(n):
    s=ord(a[i])
    pos[s]=pos[s]+1

print(pos)

y=input("enter the searc element : ")
print("occurence = ", pos[y] )
