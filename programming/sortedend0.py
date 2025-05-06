n=7
a=[int(input()) for i in range(n)]
d=[]
z=[]
for i in a :
    if i == 0 :
        z.append(i)
    else:
        d.append(i)

a=d+z
print(a)            
