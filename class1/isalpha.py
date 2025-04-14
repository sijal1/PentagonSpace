str=input("enter a string : ")
print(str)
if str.isalpha():
    print("str has only alphabets")
elif str.isdigit():
    print("str has only digits")
elif str.isalnum():
    print("str has both alphabets and digits")
else:
    print("str has special characters")            


