str=input("enter a string : ")
str1=""
for i in str:
    str1= i + str1
print(str1)
if str1==str:
    print("palindrome")
else:
    print("not a palindrome")        