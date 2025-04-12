str="   safwan is   sleeping    "
print(str)

str1=str.lstrip()
print(str1)

str2=str.rstrip()
print(str2)

str3=str.strip()
print(str3)

str5=" a d a m "
str6=""
for i in str5:
    if i == " ":
        pass
    else:
        str6=str6+i
print(str6)        