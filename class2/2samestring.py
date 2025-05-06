a=input("enter string : ")
b=input("enter string : ")
mark=0
if len(a)!=len(b):
    mark=1
else:
    for i in range(len(a)):
        if(a[i]!=b[i]):
            mark=1
if mark==0:
    print("Same")
else:
    print("not same")
                        