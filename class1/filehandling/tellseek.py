ptr=open("sijal.txt","r")

pos=ptr.tell()
print(pos)

pos1=ptr.seek(3)
print(pos1)

pos2=ptr.tell()
print(pos2)

pos3=ptr.seek(3)
print(pos3)

data=ptr.read(4)
print(data)

pos4=ptr.tell()
print(pos4)