""" str="adam is sleeping"
str1=str.split()
print(str)
print(str1)
rev=""
for i in str1:
    rev=i+" "+rev
print(rev)     """

str=input("enter string : ")
str1=str.split()
rev=""
for i in str1:
    rev=i+ " " + rev 
print(rev)    