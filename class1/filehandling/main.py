#write
name=input("enetr a name: ")
ptr=open("sijal.txt","w")
ptr.write(name)
ptr.close()
#read
str=open("sijal.txt","r")
data=str.read()
print(data)
str.close()