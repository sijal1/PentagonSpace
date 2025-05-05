a=input("enter string : ")
b=input("enter string : ")
mark=0
if len(a)!=len(b):
    mark=1
else:
    for i in a:
        if(a.count(i)!=b.count(i)):
            mark=1

if mark==0:
    print("is anagram")
else:
    print("not anaaagram")            