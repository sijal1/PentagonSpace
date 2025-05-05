class book:
    def __init__(self,page):
        self.__pages=page

    def setter(self,value):
        if value>0:
            self.__pages=value
    
    def getter(self):
        return self.__pages            
b1=book(100)

res1=b1.getter()
print(res1)

b1.setter(200)
res2=b1.getter()
print(res2)

b1.setter(-99)
res3=b1.getter()
print(res3)